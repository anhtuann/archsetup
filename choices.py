INSTALL_ENV = 'machine'
#Real install would be 'machine'

MINIMAL = ['pacaur.py',
           'cli_tools.py',
           #'virtualbox.py',
           'xserver.py',
           'backlight.py',
           'i3wm.py',
           'fs_management.py',
           'fonts.py',
           'sound.py',
           'browser.py',
           'code_env.py',
           'multimedia.py',
           'web_tools.py',
           'vim.py',
           'shell.py']

HARDWARE = ['input.py']

STEPS = list()
STEPS.extend(MINIMAL)
#STEPS.extend(HARDWARE)
