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
    '_', # Seems to be there is an empty column
    'integration_want',
    'commercial_price',
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
    ('appcode', 'appcode if it is free',): ['AppCode'],
    ('aptana studio', 'aptana studio 3', 'aptana',
     'aptana3'): ['Aptana Studio'],
    ('aptana/eclipse',): ['Aptana Studio', 'Eclipse'],
    ('aquamacs', 'emacs', 'emacs slime', 'emac',
     'emacs w/evil', 'emacs+evil mode', 'gnu emacs'): ['Emacs'],
    ('avr studio',): ['AVR Studio'],
    ('bbedit',): ['BBEdit'],
    ('bluej',): ['BlueJ'],
    ('borland c',): ['Turbo C'],
    ('brackets',): ['Brackets'],
    ('brief',): ['Brief'],
    ('canopy'): ['Canopy'],
    ('c++builder', 'c++ builder', 'cbuilder', 'borland builder'): ['C++Builder'],
    ('cf studio',): ['ColdFusion Studio'],
    ('cfeclipse',): ['CFEclipse'],
    ('chocolat', 'chocolate'): ['Chocolat'],
    ('cloud9',): ['Cloud9'],
    ('coda', 'coda 2'): ['Coda'],
    ('code::blocks', 'code:blocks', 'codeblock', 'codeblocks', 'code blocks'):
    ['Code::Blocks'],
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
    ('gedit', 'sometimes gedit is faster',): ['gedit'],
    ('gnu text edit',): ['TextEdit'],
    ('golite',): ['golite'],
    ('gvim', 'vi', 'vim', 'vim (via terminal shell)', 'macvim', 'bim',
     'vi (?, would have to look around)', 'vim?'): ['vi'],
    ('gwbasic',): ['GW-BASIC'],
    ('homesite',): ['HomeSite'],
    ('hemlock',): ['Hemlock'],
    ('idea', 'intelli j idea', 'intellij', 'intellij idea', 'intellijidea',
     'intelij idea'): ['IntelliJ IDEA'],
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
    ('leksah'): ['Leksah'],
    ('light table', 'lighttable', 'lightbox'): ['Light Table'],
    ('liteide',): ['LiteIDE'],
    ('limetext',): ['Lime'],
    ('lse',): ['LSE'],
    ('madedit',): ['MadEdit'],
    ('mantis  studio',): ['MANTIS Studio'],
    ('mathematica',): ['Mathematica'],
    ('matlab',): ['MATLAB'],
    ('mcedit',): ['MCEdit'],
    ('mg', 'microemacs'): ['MicroEMACS'],
    ('monodevelop', 'mono-d', 'mono', 'monodevelop?',): ['MonoDevelop'],
    ('mousepad',): ['Mousepad'],
    ('mplab',): ['MPLAB'],
    ('multi edit',): ['Multi-Edit'],
    ('myeclipse', 'myeclipse for spring',): ['MyEclipse'],
    ('mysql workbench',): ['MySQL Workbench'],
    ('nano',): ['nano'],
    ('nedit',): ['NEdit'],
    ('netbeans', 'netbeens', 'net beans', 'netbans', 'netbeand',
     'netbeans sucks', 'netbeans????'): ['NetBeans'],
    ('nitrous.io',): ['Nitrous.IO'],
    ('notepad', 'notepad.exe'): ['Notepad'],
    ('notepad ++', 'notepad++', 'notepad+', 'notepadd++', 'notepd++'):
    ['Notepad++'],
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
    ('qt creator', 'qt dev', 'qt-creator', 'qtcreator', 'qt designer', 'qt'):
    ['Qt Creator'],
    ('racket',): ['DrRacket'],
    ('radstudio',): ['RAD Studio'],
    ('redcar',): ['Redcar'],
    ('rstudio',): ['RStudio'],
    ('rubymine', 'rubymines'): ['RubyMine'],
    ('sas',): ['SAS'],
    ('scintilla', 'scite'): ['SciTE'],
    ('scratch',): ['Scratch'],
    ('sharpdevelop', 'sharpdevelop?'): ['SharpDevelop'],
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
     'sublimetext3', 'sublimetext3', 'sublime text + terminal', 'subl',
     'back to sublime text'):
    ['Sublime Text'],
    ('terminal (osx)'): [],
    ('text wrangler', 'textwrangle', 'textwrangler', ): ['TextWrangler'],
    ('textadept',): ['Textadept'],
    ('textastic',): ['Textastic'],
    ('textmate', 'mate', 'text mate', 'textmate 2', 'textmate 3',):
    ['TextMate'],
    ('textpad',): ['TextPad'],
    ('textwrangler/bbedit',): ['TextWrangler', 'BBEdit'],
    ('textwrangler',): ['TextWrangler'],
    ('titanium studio',): ['Titanium Studio'],
    ('toad',): ['Toad'],
    ('turbo c++',): ['Turbo C++'],
    ('turbo pascal ide', 'turbo pascal', 'borland ide (during dos days)',
     'borland'): ['Turbo Pascal'],
    ('ultraedit', 'ultra edit'): ['UltraEdit'],
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
    ('wingide', 'wing', 'wing ide'): ['WingIDE'],
    ('wordpad',): ['WordPad'],
    ('wps',): ['WPS Workbench'],
    ('xamarin studio',): ['Xamarin Studio'],
    ('xamarin studio / monodevelop',): ['Xamarin Studio', 'MonoDevelop'],
    ('xcode', 'x code'): ['Xcode'],
    ('yi',): ['Yi'],
    ('zend', 'zend studio'): ['Zend Studio'],
    ('zile',): ['Zile'],
    ('sublime or emacs',
     'try getting used to emacs again, otherwise sublime text 3',):
    ['Sublime Text', 'Emacs'],
    ('sublime or vim',): ['Sublime Text', 'vi'],
    ('sublime, maybe pycharm',): ['Sublime Text', 'PyCharm'],
    ('padre, or perhaps write my own',): ['Padre'],
    ('pycharm, rubymine'): ['PyCharm', 'RubyMine'],
    ('chocolat or sublime text',): ['Chocolat', 'Sublime Text'],
    ('gedit or geany, probably. depends on the task.',): ['gedit', 'Geany'],
    ('gedit, notepad++',): ['gedit', 'Notepad++'],
    ('notepad ++; qt creator'): ['Notepad++', 'QtCreator'],
    ('notepad++ or code::blocks',): ['Notepad++', 'Code::Blocks'],
    ('revolution analytics, sas',): ['Revolution Analytics', 'SAS'],
    ('?', 'ahhh!', 'any text editor', "don't know", "i don't know", 'no idea',
     'i have no idea', "i'd program my own", "it won't.", 'no clue (for c#)',
     "don't know at this point, would have to research", 'no idea!', 'none',
     'that is not going to happen.', "vim has been around in one form or "
     "another since 1976! it's not going any where ;-)", "vim won't desappear, "
     "it's been here before me, and will be here after me ;]", "don't know",
     'dunno', 'haha ... good one :)', 'magnetize neadle', 'my own', 'my penis',
      'no idea', 'no more', 'none', 'not sure', "oh dear god, why would you "
     "do that?", 'oh god no!', 'opensouce does not disappear', 'something '
     "lightweight i can use from the terminal", 'write my own'): ["Don't know"],
    ('another vi-variant', 'any reasonable emacs clone/fork',
     'anything that supports vim bindings', 'use another vi clone.',
     'xemacs'): ['Something similar']
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


INTEGRATION_MAP = {
    ('aesthetics',): ['ui'],
    ('auto-completion', 'intellisense',): ['auto_completion'],
    ('better support for more languages',
     'better auto-completion in javascript with libraries.',):
    ['many_languages'],
    ('build tool(s) integration',): ['build_tool_integration'],
    ('code formatting',): ['code_formatting'],
    ('code generation',): ['code_generation'],
    ('debugging', 'linting tools integration', 'find bugs',): ['debugging'],
    ('documentation for language or libraries inside the editor',): ['docs'],
    ('extensibility', 'better macros', 'macros', 'plugins',
     'id like grammar based language mode definitions', ): ['extensibility'],
    ('fast',): ['speed'],
    ('i prefer minimal integration.',): ['lightweightness'],
    ('interactive console/repl',): ['console'],
    ('language aware navigation and editing', 'navigation', 'code navigation',
     'better file navigation', 'better file navigation',
     'project navigation',
     'semantics searching capabilities'): ['code_navigation'],
    ('n/a', 'na', 'nil', 'no idea', 'none', 'none of the above',
     'none of these', 'none?', 'nothing', 'nothing. vs has everything i need.',
     'pretty much has all of the above', 'vim is great', 'i am happy', 'done',
     'things are sufficiently provided by plugins', 'cant think of any',
     'emacs has all of this', 'it has everything', '???', 'all are quite good',
     'it has it all (idea)', 'im really happy with all of these in idea',):
    ['none'],
    ('refactoring',): ['refactoring'],
    ('speed and easy of use', 'speed of loading',
     'performance improvement',): ['speed'],
    ('stability',): ['dependability'],
    ('syntax highlighting',): ['syntax_highlighting'],
    ('test integration',): ['test_integration'],
    ('vcs integration', 'version control integration',
     'version control integration is very poor',): ['vcs integration'],
    ('vim suppor'): ['powerful_editing'],
}


SECONDARY_REASON_MAP = {
    ('it supports some of the languages i use better than my primary editor',
     'it is a also framework to develop rich client applications',
     'visual studio intellisense', 'platform specific',
     'support for a different subset of languages.',
     'better debugging', 'debug', 'debuggin', 'debugging',
     'interactive debugger', 'rubymine has an incredible integrated debugger',):
    ['better_language_support'],
    ('it supports the build tools or building proccess that i use better',
     'apple dictates', 'for windows programming', 'run better on windows',
     'i have to use it for ios development', 'ios development requires xcode',
    'supports a different os',):
    ['better_build_support'],
    ('it can be used from terminal',):
    ['terminal'],
    ("it doesn't build project on every save", "it's better for editing text.",
     "it's faster to us!e for small editing", 'fast startup', "it's fast.",
     'sometimes domt want to clog up my buffers for a small change',):
    ['faster_for_small'],
    ('i use it for editing code on remote servers',
     'not available on remote server',):
    ['remote_editing'],
    ('available on office', 'forced to use eclipse by work',
     'i can use them from my work pc.', 'i had to', 'i have to',
     "i'm forced to do so.", "i'm its current primary developer.",
     'idea was paid by my startup', 'no choice',
     'required by my client', 'working on peer reviews',
     'the team uses netbeans', 'team uses it',
     'it is not installed on some systems', "i'm on other peoples' computers",
     'different os at home', 'force majeure', 'i use it in windows',
     'i use them on a system where my primary editor is not available.',
     "my editor isn't available", 'no vim installed?',
     'pair programming with people who use other editors',
     'pairing with someone unfamiliar with vim.',):
    ['primary_not_available'],
    ('better file search ability', 'better find/replace with regex',
     'better search and navigation across files',
     "doen't leave the ~ files around", 'faster/better file finder',
     'it has some tools unavailable in my primary',
     'non-build features like ediff and dired',
     'multiple cursor select!', 'it looks nicer',
     'interactive repl', 'graphics',
     'advanced text editing features', 'allows for better free form writing',):
    ['better_other_feature'],
    ('but easier in st3 or idea.', 'curiosity', 'for the exercise',):
    ['other'],
    ("i don't use other editors.", "i don't use anything else",
     "i don't use other editors/ides", 'i very rarely use others.',
     "i haven't explored vim completely as of now."
     " those things are possible in vim", 'only use primary',
     'only use others if i absolutely have to',
     'occasionally', 'too many questions',): [],
 }


COMMERCIAL_USE = {
    'Yes, I have personally bought it': 'self',
    'Yes, my employer bought it': 'employer',
    'No, but I tried trial versions': 'trial',
    'No, never': 'never',
}


COMMERCIAL_USE_POTENTIAL = {
    'Yes, I would buy it myself': 'self',
    'Yes, if my employer buys it for me': 'employer',
    'No': 'never'
}


VCS_USE = {
    'From the primary editor': 'primary_editor',
    'From one of the non-primary editors' : 'secondary_editor',
    'From some other application': 'other_app',
    'Directly through terminal' : 'terminal',
    'Other' : 'other'
}


CUSTOMIZATION = {
    "It's almost the same from the stock configuration": 'low',
    "There is some configuration and couple of third-party plugins": 'medium',
    "It is extensively configured and I have lots of third-party plugins": 'high'
}


COMPANY_PROGRAMMING_INVOLVEMENT = {
    'Is primarily doing programming': 'software',
    "Does programming as part of it's core activities": 'software_related',
    'Sometimes supports other activities with programming or IT': 'other',
    'I am a researcher': 'researcher',
    'I am a student or unemployed': 'student_unemployed',
    'My primary job is something else than programming': 'non_programmer'
}
