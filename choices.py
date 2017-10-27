INSTALL_ENV = 'machine'
#Real install would be 'machine'

MINIMAL = ['pacaur.py',
           'i3wm.py',
           'fonts.py',
           'code_env.py',
           'web_dev.py',
           'vim.py',
           'shell.py']

SERVERS = ['lemp.py',
           'matrix.py']

STEPS = list()
STEPS.extend(MINIMAL)
STEPS.extend(SERVERS)
