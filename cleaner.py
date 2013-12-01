import sys
import csv
from collections import OrderedDict
from itertools import izip


def tails(iterable):
    tail = list(iterable)
    for item in tail:
        yield tail
        tail = tail[1:]


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


multiple_columns = set(tail[0] for tail in tails(HEADERS)
                       if len(tail) > 1 and tail[0] == tail[1])
flat_columns = set(header for header in HEADERS
                   if header not in multiple_columns)


# FEATURES_MAP = {
#     ('')
# }


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


EDITOR_MAP = {
    ('android studio', 'androidstudio'): ['Android Studio'],
    ('appcode',): ['AppCode'],
    ('aptana studio',): ['Aptana Studio'],
    ('aquamacs', 'emacs', 'emacs slime'): ['Emacs'],
    ('bbedit',): ['BBEdit'],
    ('bim',): ['bim'],
    ('bluej',): ['BlueJ'],
    ('brackets',): ['Brackets'],
    ('chocolat',): ['Chocolat'],
    ('cloud9',): ['Cloud9'],
    ('coda', 'coda 2'): ['Coda'],
    ('code::blocks', 'code:blocks', 'codeblocks'): ['Code::Blocks'],
    ('codelite',): ['CodeLite'],
    ('crudzilla web application builder (our company product)',): ['crudzilla'],
    ('ecilpse', 'eclipse'): ['Eclipse'],
    ('ed',): ['ed'],
    ('flash builder',): ['Flash Builder'],
    ('geany',): ['Geany'],
    ('gedit', 'sometimes gedit is faster',): ['Gedit'],
    ('golite',): ['golite'],
    ('gvim', 'vi', 'vim', 'vim (via terminal shell)', 'macvim'): ['vi'],
    ('idea', 'intelli j idea', 'intellij', 'intellij idea', 'intellijidea'):
     ['IntelliJ IDEA'],
    ('idle'): ['IDLE'],
    ('ipython notebook',): ['iPython Notebook'],
    ('ise', 'powershell ise'): ['PowerShell ISE'],
    ('jade',): ['Jade'],
    ('jed',): ['JED'],
    ('kate',): ['Kate'],
    ('kdevelop',): ['KDevelop'],
    ('komodo', 'komodo edit', 'komodo ide'): ['Komodo'],
    ('light table', 'lighttable'): ['Light Table'],
    ('liteide',): ['LiteIDE'],
    ('mantis  studio',): ['MANTIS Studio'],
    ('matlab',): ['MATLAB'],
    ('mcedit',): ['MCEdit'],
    ('mg', 'microemacs'): ['MicroEMACS'],
    ('monodevelop', 'mono-d',): ['MonoDevelop'],
    ('mousepad',): ['Mousepad'],
    ('myeclipse', 'myeclipse for spring',): ['MyEclipse'],
    ('mysql workbench',): ['MySQL Workbench'],
    ('nano',): ['nano'],
    ('netbeans', 'netbeens',): ['NetBeans'],
    ('nitrous.io',): ['Nitrous.IO'],
    ('notepad',): ['Notepad'],
    ('notepad ++', 'notepad++'): ['Notepad++'],
    ('notepad2',): ['Notepad2'],
    ('objective-c',): ['objective-c'],
    ('php storm', 'phpstorm',): ['PhpStorm'],
    ('pl\sql developer',): ['PL/SQL Developer'],
    ('powerbuilder',): ['PowerBuilder'],
    ("programmer's notepad",): ["Programmer's Notepad"],
    ('pspad',): ['PSPad'],
    ('pycharm',): ['PyCharm'],
    ('pyscripter',): ['pyscripter'],
    ('qt creator', 'qt dev', 'qt-creator', 'qtcreator'): ['Qt Creator'],
    ('rstudio',): ['RStudio'],
    ('rubymine',): ['RubyMine'],
    ('sas',): ['SAS'],
    ('scratch',): ['Scratch'],
    ('slickedit',): ['SlickEdit'],
    ('spyder',): ['Spyder'],
    ('sql pro',): ['SequelPro'],
    ('subime', 'subime text','sublime', 'sublime 2', 'sublime text',
     'sublime text  2', 'sublime text 2', 'sublime text 3',
     'sublime text 3 beta', 'sublime text editor', 'sublime-text',
     'sublimetext', 'sublimetext 2', 'sublimetext 3', 'sublimetext2',
     'sublimetext3'): ['Sublime Text'],
    ('text wrangler', 'textwrangle','textwrangler', ): ['TextWrangler'],
    ('textadept',): ['Textadept'],
    ('textmate', 'mate', 'text mate'): ['TextMate'],
    ('textwrangler/bbedit',): ['TextWrangler', 'BBEdit'],
    ('titanium studio',): ['Titanium Studio'],
    ('visual studio', 'visual studio .net', 'visual studio 2012',
     'visual studio express', 'visual studio.net', 'visual studios',
     'visual studios 2010', 'visualstudio', 'ms visual studio',
     'ms visual studio 2010', 'vb express 2008',
     'sql server management studio', 'ssms'):
    ['Visual Studio'],
    ('web matrix',): ['WebMatrix'],
    ('web storm', 'webstorm'): ['WebStorm'],
    ('windriver workbench',): ['Wind River Workbench'],
    ('wingide',): ['WingIDE'],
    ('wps',): ['WPS Workbench'],
    ('xamarin studio',): ['Xamarin Studio'],
    ('xcode',): ['XCode'],
    ('yi',): ['Yi'],
    ('zend',): ['Zend Studio'],
    ('zile',): ['Zile'],
}


VCS_MAP = {
    ('bazaar', 'bzr',): ['Bazaar'],
    ('ca workbench',): ['CA Workbench'],
    ('clearcase',): ['ClearCase'],
    ('copy and paste', "i don't use one", 'none','my own',
     'omg i dont even know what that is sorry',
     'zip & upload to google drive', 'osx', 'sharepoint',
     'linux', 'debian',): ['None'],
    ('cvs',): ['CVS'],
    ('darcs',): ['darcs'],
    ('even split between mercurial and git', 'git, hg',): ['Git', 'Mercurial'],
    ('fossil scm',): ['Fossil SCM'],
    ('git', 'git with gitlab', 'git/github', 'github', 'giy',): ['Git'],
    ('git & svn - 50/50', 'svn at work, git at home', 'svn, git',):
    ['Git', 'Subversion'],
    ('hg', 'mercurial',): ['Mercurial'],
    ('perforce', 'source depot',): ['Perforce'],
    ('starteam',): ['StarTeam'],
    ('subversion', 'svn', 'tortoisesvn',): ['Subversion'],
    ('team foundation server', 'tfs'): ['TFS'],
    ('tfs and git',): ['TFS', 'Git'],
    ('tfs, subversion',): ['TFS', 'Subversion'],
    ('unity asset server',): ['Unity Asset Server'],
    ('vault',): ['Vault'],
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
    for names, real_name in VCS_MAP.items():
        vcs = row['vcs']
        if len(vcs) < 2:
            if vcs[0].lower().strip() in names:
                row['vcs'] = real_name


def clean_editors(row):
    for names, real_name in EDITOR_MAP.items():
        p_e = row['primary_editor'][0]
        if p_e.lower().strip() in names:
            row['primary_editor'] = real_name

        new_e = []
        for editor in row['secondary_editor']:
            e = editor.lower().strip()
            if e:
                if e in names:
                    new_e.extend(real_name)
                else:
                    new_e.append(editor)
        row['secondary_editor'] = new_e

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
    clean_vcs(row)
    # Clean editors
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
                            for header in multiple_columns]
    for row in rows:
        for header in flat_columns:
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
