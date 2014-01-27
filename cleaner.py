import sys
import csv
from collections import OrderedDict
from itertools import izip
from constants import *


# Utils

def tails(iterable):
    tail = list(iterable)
    for item in tail:
        yield tail
        tail = tail[1:]


def multiple_columns():
    return set(LIST_ANSWERS) | set(tail[0] for tail in tails(HEADERS)
                                   if len(tail) > 1
                                   and tail[0] == tail[1])


def flat_columns():
    return set(header for header in HEADERS
               if header not in multiple_columns)


# Main logic

def read_csv(filename):
    result = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        next(reader)  # Skip header
        for row in reader:
            row_dict = OrderedDict()
            for key, value in izip(HEADERS, row):
                existing = row_dict.get(key, [])
                existing.append(value)
                row_dict[key] = existing
            result.append(row_dict)
    return result


def clean_mp_answers(row):
    replacements = {
        '(eg auto-completion, refactoring, building)':
        '(eg auto-completion; refactoring; building)',
        '(eg. go to definition, find uses)':
        '(eg go to definition; find uses)',
        '(go to definition, find uses)':
        '(go to definition; find uses)',
        'better integration into other, non-development tools':
        'better integration into other; non-development tools',
        'High configurability, though very tedious to extensively customize':
        'High configurability; though very tedious to extensively customize',
        'smaller, tighter install':
        'smaller; tighter install'
    }

    def replace(s, mapping):
        for k, v in mapping.items():
            s = s.replace(k, v)
        return s

    for answer_key in ['features_value', 'features_want']:
        row[answer_key] = [replace(row[answer_key][0], replacements)]


def create_lists(row):
    for list_answer in LIST_ANSWERS:
        row[list_answer] = [r.strip() for r in row[list_answer][0].split(',')]


def clean_by_map(name_map, headers, row):
    for names, real_name in name_map.items():
        for header in headers:
            new_values = []
            for value in row[header]:
                v = value.lower().strip()
                if v:
                    if v in names:
                        new_values.extend(real_name)
                    else:
                        new_values.append(value.strip())
            row[header] = new_values


def clean_working_hours(row):
    pass


def clean_languages(row):
    for names, real_name in LANGUAGE_MAP.items():
        new_l = []
        for language in row['languages']:
            l = language.lower().strip()
            if l:
                if l in names:
                    new_l.extend(real_name)
                else:
                    new_l.append(language)
        row['languages'] = new_l


def clean_vcs(row):
    for names, real_name in VCS_MAP.items():
        vcs = row['vcs']
        if len(vcs) < 2:
            if vcs[0].lower().strip() in names:
                row['vcs'] = real_name


def clean_editors(row):
    for names, real_name in EDITOR_MAP.items():
        for header in ('primary_editor', 'secondary_editor',
                       'ex_editors', 'alternative_primary'):
            new_e = []
            for editor in row[header]:
                e = editor.lower().strip()
                if e:
                    if e in names:
                        new_e.extend(real_name)
                    else:
                        new_e.append(editor)
            row[header] = new_e


def clean_row(row):
    clean_mp_answers(row)
    create_lists(row)
    clean_by_map(FEATURES_MAP, ('features_value', 'features_want'), row)
    clean_by_map(INTEGRATION_MAP,
                 ('integration_value', 'integration_want'),
                 row)
    clean_by_map(SECONDARY_REASON_MAP, ('secondary_editor_reason',), row)
    #clean_working_hours(row)
    clean_languages(row)
    clean_vcs(row)
    clean_editors(row)


def clean(rows):
    for row in rows:
        clean_row(row)
    return rows


def get_all_values(rows, header):
    return sorted(set(value for row in rows
                            for value in row[header]))


def normalize(rows):
    multiple_columns_map = [(header, get_all_values(rows, header))
                            for header in multiple_columns()]
    for row in rows:
        for header in flat_columns():
            row[header] = row[header][0]
        for header, values in multiple_columns_map:
            for value in values:
                row[header + '.' + value] = False
            for value in values:
                if row[header] == value:
                    row[header + '.' + value] = True
            del row[header]
    return rows


def get_headers(result_line):
    return result_line.keys()


def stringify(result_line):
    return result_line.values()


def main(filename):
    raw = read_csv(filename)
    cleaned = clean(raw)
    normalized = normalize(cleaned)

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
    writer.writerow(get_headers(normalized[0]))
    for line in normalized:
        writer.writerow(stringify(line))


if __name__ == "__main__":
    main(sys.argv[1])
