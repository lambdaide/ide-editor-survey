import sys
import csv
from collections import OrderedDict
from itertools import izip


HEADERS = [
    'hours_work',
    'hours_studying',
    'hours_hobby',
    'languages',
    'languages',
    'languages',
    'vcs',
    'company_programming_involvement',
    'primary_editor',
    'secondary_editor',
    'secondary_editor',
    'secondary_editor',
    'ex_editors',
    'ex_editors',
    'ex_editors',
    'features_value',
    'integration_value',
    'features_want',
    'customization',
    'secondary_editor_reason',
    'vcs_use',
    'not_switching_reasons',
    'alternative_primary',
    'commercial_use',
    'commercial_potential_use',
    'commercial_price',
    'integration_want',
]


LIST_ANSWERS = [
    'features_value',
    'integration_value',
    'features_want',
    'secondary_editor_reason',
    'not_switching_reasons',
    'integration_want',
]


FEATURES_MAP = {
    ('')
}


LANGUAGE_MAP = {
    ('.net', 'c#', 'c# .net', 'c sharp',): ['C#'],
    ('asp',): ['ASP'],
    ('absl', ): ['SAP'],
    ('apt', ): ['APT'],
    ('actionscript', 'flex (as3)'): ['ActionScript'],
    ('ada05', ): ['Ada'],
    ('apex', ): ['APEX'],
    ('assembly', 'x86 assembly', 'mips'): ['Assembly'],
    ('bash', 'sh', 'shell', 'shell script', 'powershell'): ['Shell'],
    ('c',): ['C'],
    ('c / c++', 'c/c++'): ['C', 'C++'],
    ('c++',): ['C++'],
    ('cg',): ['Cg'],
    ('clojure',): ['Clojure'],
    ('coffeescript',): ['CoffeeScript'],
    ('commonlisp', 'common lisp'): ['Common Lisp'],
    ('camel dsl',): ['Apache Camel DSL'],
    ('coldfusion',): ['ColdFusion'],
    ('css', 'css3'): ['CSS'],
    ('html/css',): ['HTML', 'CSS'],
    ('d',): ['D'],
    ('dart',): ['Dart'],
    ('dylan',): ['Dylan'],
    ('elisp', 'emacs lisp'): ['Emacs Lisp'],
    ('elm',): ['Elm'],
    ('erlang',): ['Erlang'],
    ('forth',): ["Forth"],
    ('fortran',): ['Fortran'],
    ('go', 'golang'): ['Go'],
    ('groovy',): ['Groovy'],
    ('haskell',): ['Haskell'],
    ('html', 'html5'): ['HTML'],
    ('jade',): ['Jade'],
    ('java',  'java currently, otherwise anything new'): ['Java'],
    ('java script', 'javascript', 'javascript (inc node)', 'js', 'js/jquery',
     'node', 'node.js', 'nodejs'): ['JavaScript'],
    ('julia',): ['Julia'],
    ('latex',): ['LaTeX'],
    ('lisp',): ['Lisp'],
    ('lua',): ['Lua'],
    ('mantis',): ['MANTIS'],
    ('mathscript',): ['MathScript'],
    ('matlab',): ['MATLAB'],
    ('objective c', 'objective-c', 'objectivec'): ['Objective C'],
    ('ocaml',): ['OCamL'],
    ('perl',): ['Perl'],
    ('php',): ['PHP'],
    ('pl/sql', 'pl\\sql'): ['PL/SQL'],
    ('powerbuilder 11',): ['PowerBuilder 11'],
    ('prolog',): ['Prolog'],
    ('python', 'python3'): ['Python'],
    ('qlang',): ['Qlang'],
    ('r',): ['R'],
    ('racket',): ['Racket'],
    ('ruby',): ['Ruby'],
    ('rust',): ['Rust'],
    ('sas',): ['SAS'],
    ('sass',): ['SASS'],
    ('scala',): ['Scala'],
    ('scheme',): ['Scheme'],
    ('sql',): ['SQL'],
    ('tcl',): ['Tcl'],
    ('vb.net', 'visual basic', 'vba'): ['Visual Basic'],
    ('verilog',): ['Verilog'],
    ('vhdl',): ['VHDL'],
    ('viml',): ['VimL']
}




def read_csv(filename):
    result = []
    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        next(reader) # Skip header
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
        '(eg auto-completion refactoring building)',
        '(go to definition, find uses)':
        '(go to definition, find uses)',
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
    pass


def clean_editors(row):
    pass


def clean_row(row):
    # Clean up multiple answers
    clean_mp_answers(row)
    # Create lists where applicable
    create_lists(row)
    # Unify working hours
    #clean_working_hours(row)
    # Clean programming languages
    clean_languages(row)
    # Clean VCS
    #clean_vcs(row)
    # Clean editors
    #clean_editors(row)


def clean(rows):
    for row in rows:
        clean_row(row)
    return rows


def stringify(result_line):
    pass


def main(filename):
    raw = read_csv(filename)
    cleaned = clean(raw)

    writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
    writer.writerow(get_headers())
    for line in cleaned:
        writer.writerow(stringify(line))


if __name__ == "__main__":
    main(sys.argv[1])
