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
                       if len(tail) > 1 and tail[0] == tail[1]) | set(LIST_ANSWERS)
flat_columns = set(header for header in HEADERS
                   if header not in multiple_columns)


FEATURES_MAP = {
    ('crossplateform',
     'cross platform',):
        ['portability'],
    ('be less weird',
     'shorter learningcurve',):
        ['easy_to_learn'],
    ('being rock solid',
     'less bugs',
     'less errors',
     'stability',):
        ['dependability'],
    ('better built in web browser (serious)r',):
        ['builtin_web_browser'],
    ('better colors/theme support',):
        ['themes'],
    ('better integration into other; non-development tools'):
        ['other_integration'],
    ('cloud support - still annoying that i can\'t just "keep working" on'
     ' another machine.',
     'client/server model (share sessions between different instances)',):
        ['persistent_remote_sessions'],
    ('composability: components that work '
     'together \xc3\xa0 la most emacs modes',
     'easier plugin development',
     'modern scripting language',
     'better scripting language',
     'macros',
     'better macros',):
        ['extensibility'],
    ('console/debugger',):
        ['console', 'advanced_language_integration'],
    ('emacs has every feature i want',
     'i am happy with it',
     'is there anything vim cant do?',
     'it has all of those things already',
     'n/a', 'na', 'none', 'none.', '?',
     "none i use emacs anything it doesn't do i can make it do",
     "none. i'm satisfied with its current feature set.",
     'nothing', 'no idea', 'vim is great', 'abc', 'it has it all (idea)',
     'kitchen sink', 'pycharm has everything', 'threads',
     'vimscript+python is enough to add any features i require'):
        [],
    ('foss',):
        ['open_source'],
    ('interactive console/repl',
     'proper emacs-style repl',
     'better console integration',):
        ['console'],
    ('it can be used in terminal', 'it can be used it in terminal',
     'ability to use it in terminal'):
        ['terminal_usage'],
    ("it doesn't need to be configured much to be usable",
     'better default configuration'):
        ['usable_out_of_the_box'],
    ('it has advanced language intergration'
     ' (eg auto-completion; refactoring; building)',
     'it has advanced language integration'
     ' (eg auto-completion; refactoring; building)',
     'advanced language intergration'
     ' (eg auto-completion; refactoring; building)',
     'debugger features',
     'better debugging integration',
     'debugging',
     'official c++ support',
     'refactoring',
     'something like slime for emacs',
     'formatting for javascript leading commas',
     'lisp syntax completion',):
        ['advanced_language_integration'],
    ('it intergrates to build tool(s) that i use',
     'build tools integration',
     'better working build tools',
     'integration to build tool(s) that i use',):
        ['build_tool_integration'],
    ('it intergrates with version control system',
     'integration with version control system',):
        ['version_control_integration'],
    ('it is very configurable',
     'configurability',
     'easier configuration',
     'high configurability; though very tedious to extensively customize',):
        ['configurability'],
    ('it provides good tools for navigating the code'
     ' (eg go to definition; find uses)',
     'tools to navigate the code (go to definition; find uses)',):
        ['code_navigation'],
    ('it starts up and works very fast',
     'faster start up and overall performance',
     'asyncronous operations',):
        ['speed'],
    ('it supports many programming languages',
     'support for many programming languages',):
        ['many_languages'],
    ('kio slaves',
     'ssh/ftp integration',
     'better remote code',):
        ['remote_editing'],
    ('lower cost',):
        ['low_cost'],
    ('powerful editing functionality', 'vim emulation mode',):
        ['powerful_editing'],
    ('powerful search & discovery tools; (could be part either of powerful'
     ' editing or adv. lang. integration)',):
        ['powerful_editing', 'advanced_language_integration'],
    ('smaller; tighter install',):
        ['lightweight'],
    ('snippets',):
        ['code_generation'],
    ('splits',):
        ['ui'],
    ('there are lots of plugins available',
     'rich plugins ecosystem',
     'non-java plugins',
     'specific plugins (eg. better android support)',):
        ['many_plugins'],
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


EDITOR_MAP = {
    ('ace',): ['Ace'],
    ('allegrocl',): ['Allegro CL'],
    ('android studio', 'androidstudio'): ['Android Studio'],
    ('appcode',): ['AppCode'],
    ('aptana studio', 'aptana studio 3', 'aptana', 'aptana3'): ['Aptana Studio'],
    ('aptana/eclipse',): ['Aptana Studio', 'Eclipse'],
    ('aquamacs', 'emacs', 'emacs slime'): ['Emacs'],
    ('avr studio',): ['AVR Studio'],
    ('bbedit',): ['BBEdit'],
    ('bluej',): ['BlueJ'],
    ('borland c',): ['Turbo C'],
    ('brackets',): ['Brackets'],
    ('brief',): ['Brief'],
    ('c++builder', 'c++ builder', 'cbuilder', 'borland builder'): ['C++Builder'],
    ('cf studio',): ['ColdFusion Studio'],
    ('cfeclipse',): ['CFEclipse'],
    ('chocolat', 'chocolate'): ['Chocolat'],
    ('cloud9',): ['Cloud9'],
    ('coda', 'coda 2'): ['Coda'],
    ('code::blocks', 'code:blocks', 'codeblock', 'codeblocks', 'code blocks'): ['Code::Blocks'],
    ('code composer studio',): ['Code Composer Studio'],
    ('codebeans (university ide)',): ['Codebeans'],
    ('codelite',): ['CodeLite'],
    ('codewarrior',): ['CodeWarrior'],
    ('crudzilla web application builder (our company product)',): ['crudzilla'],
    ('dev-c++',): ['Dev-C++'],
    ('dev studio',): ['DevStudio'],
    ('dreamweaver',): ['Dreamweaver'],
    ('e texteditor',): ['E Text Editor'],
    ('ecilpse', 'eclipse'): ['Eclipse'],
    ('ed',): ['ed'],
    ('editplus',): ['EditPlus'],
    ('edlin',): ['Edlin'],
    ('edt',): ['EDT'],
    ('embedded ides: matlab, texmaker'): ['MATLAB', 'Texmaker'],
    ('embedded workbench', 'iar embedded workbench'): ['Embedded Workbench'],
    ('espresso',): ['Espresso'],
    ('flash builder',): ['Flash Builder'],
    ('fraise',): ['Fraise'],
    ('fte',): ['FTE'],
    ('geany',): ['Geany'],
    ('gedit', 'sometimes gedit is faster',): ['Gedit'],
    ('gnu text edit',): ['TextEdit'],
    ('golite',): ['golite'],
    ('gvim', 'vi', 'vim', 'vim (via terminal shell)', 'macvim', 'bim'): ['vi'],
    ('gwbasic',): ['GW-BASIC'],
    ('homesite',): ['HomeSite'],
    ('idea', 'intelli j idea', 'intellij', 'intellij idea', 'intellijidea', 'intelij idea'):
     ['IntelliJ IDEA'],
    ('idle'): ['IDLE'],
    ('intype',): ['Intype'],
    ('ipython notebook',): ['IPython Notebook'],
    ('ise', 'powershell ise'): ['PowerShell ISE'],
    ('jade',): ['Jade'],
    ('jbuilder',): ['JBuilder'],
    ('jdeveloper',): ['JDeveloper'],
    ('jed',): ['JED'],
    ('jedit',): ['jEdit'],
    ('jgrasp',): ['jGRASP'],
    ('joe',): ['JOE'],
    ('kate',): ['Kate'],
    ('kdevelop',): ['KDevelop'],
    ('komodo', 'komodo edit', 'komodo ide', 'activestate komodo'): ['Komodo'],
    ('light table', 'lighttable', 'lightbox'): ['Light Table'],
    ('liteide',): ['LiteIDE'],
    ('lse',): ['LSE'],
    ('madedit',): ['MadEdit'],
    ('mantis  studio',): ['MANTIS Studio'],
    ('mathematica',): ['Mathematica'],
    ('matlab',): ['MATLAB'],
    ('mcedit',): ['MCEdit'],
    ('mg', 'microemacs'): ['MicroEMACS'],
    ('monodevelop', 'mono-d',): ['MonoDevelop'],
    ('mousepad',): ['Mousepad'],
    ('mplab',): ['MPLAB'],
    ('multi edit',): ['Multi-Edit'],
    ('myeclipse', 'myeclipse for spring',): ['MyEclipse'],
    ('mysql workbench',): ['MySQL Workbench'],
    ('nano',): ['nano'],
    ('nedit',): ['NEdit'],
    ('netbeans', 'netbeens', 'net beans', 'netbans', 'netbeand', 'netbeans sucks'): ['NetBeans'],
    ('nitrous.io',): ['Nitrous.IO'],
    ('notepad', 'notepad.exe'): ['Notepad'],
    ('notepad ++', 'notepad++', 'notepad+', 'notepadd++', 'notepd++'): ['Notepad++'],
    ('notepad2',): ['Notepad2'],
    ('padre',): ['Padre'],
    ('php storm', 'phpstorm',): ['PhpStorm'],
    ('phped',): ['PhpED'],
    ('pl\sql developer',): ['PL/SQL Developer'],
    ('powerbuilder',): ['PowerBuilder'],
    ("programmer's notepad", "Programmer's Notepad 2"): ["Programmer's Notepad"],
    ('pspad',): ['PSPad'],
    ('pycharm',): ['PyCharm'],
    ('pyscripter',): ['pyscripter'],
    ('pythonwin',): ['PythonWin'],
    ('qbasic ide',): ['QBasic'],
    ('qt creator', 'qt dev', 'qt-creator', 'qtcreator', 'qt designer', 'qt'): ['Qt Creator'],
    ('racket',): ['DrRacket'],
    ('radstudio',): ['RAD Studio'],
    ('redcar',): ['Redcar'],
    ('rstudio',): ['RStudio'],
    ('rubymine', 'rubymines'): ['RubyMine'],
    ('sas',): ['SAS'],
    ('scintilla', 'scite'): ['SciTE'],
    ('scratch',): ['Scratch'],
    ('slickedit',): ['SlickEdit'],
    ('spider',): ['Spider Writer'],
    ('spyder',): ['Spyder'],
    ('sql pro',): ['SequelPro'],
    ('sql developer'): ['SQL Developer'],
    ('sql server management studio', 'ssms'): ['SQL Server Management Studio'],
    ('subime', 'subime text', 'sublime', 'sublime 2', 'sublime text',
     'sublime text  2', 'sublime text 2', 'sublime text 3',
     'sublime text 3 beta', 'sublime text editor', 'sublime-text',
     'sublimetext', 'sublimetext 2', 'sublimetext 3', 'sublimetext2',
     'sublimetext3'): ['Sublime Text'],
    ('terminal (osx)'): [],
    ('text wrangler', 'textwrangle', 'textwrangler', ): ['TextWrangler'],
    ('textadept',): ['Textadept'],
    ('textastic',): ['Textastic'],
    ('textmate', 'mate', 'text mate', 'textmate 2'): ['TextMate'],
    ('textpad',): ['TextPad'],
    ('textwrangler/bbedit',): ['TextWrangler', 'BBEdit'],
    ('textwrangler',): ['TextWrangler'],
    ('titanium studio',): ['Titanium Studio'],
    ('toad',): ['Toad'],
    ('turbo c++',): ['Turbo C++'],
    ('turbo pascal ide', 'turbo pascal', 'borland ide (during dos days)', 'borland'): ['Turbo Pascal'],
    ('ultraedit',): ['UltraEdit'],
    ('visual studio', 'visual studio .net', 'visual studio 2012',
     'visual studio express', 'visual studio.net', 'visual studios',
     'visual studios 2010', 'visualstudio', 'ms visual studio',
     'ms visual studio 2010', 'vb express 2008', 'visual c++', 'visual dsp++',
     'visual studio 2005/2008/2010',): ['Visual Studio'],
    ('visual dsp++',): ['VisualDSP++'],
    ('visual slickedit',): ['SlickEdit'],
    ('web matrix',): ['WebMatrix'],
    ('web storm', 'webstorm'): ['WebStorm'],
    ('windriver workbench',): ['Wind River Workbench'],
    ('wingide',): ['WingIDE'],
    ('wordpad',): ['WordPad'],
    ('wps',): ['WPS Workbench'],
    ('xamarin studio',): ['Xamarin Studio'],
    ('xamarin studio / monodevelop',): ['Xamarin Studio', 'MonoDevelop'],
    ('xcode', 'x code'): ['Xcode'],
    ('yi',): ['Yi'],
    ('zend', 'zend studio'): ['Zend Studio'],
    ('zile',): ['Zile'],
}


VCS_MAP = {
    ('bazaar', 'bzr',): ['Bazaar'],
    ('ca workbench',): ['CA Workbench'],
    ('clearcase',): ['ClearCase'],
    ('copy and paste', "i don't use one", 'none', 'my own',
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


def clean_features(row):
    for names, real_name in FEATURES_MAP.items():
        for header in ('features_value', 'features_want'):
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
        for header in ('primary_editor', 'secondary_editor', 'ex_editors'):
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
    # Clean up multiple answers
    clean_mp_answers(row)
    # Create lists where applicable
    create_lists(row)
    # Clean valued and wanted features
    clean_features(row)
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
