INSTALL_ENV = 'machine'
#Real install would be 'machine'

MINIMAL = ['fonts.py',
           'vim.py',
           'shell.py']

TOOLS = ['fs_management.py']

SERVERS = ['lemp.py',
           'matrix.py']

STEPS = list()
STEPS.extend(MINIMAL)
STEPS.extend(TOOLS)
#STEPS.extend(SERVERS)
