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
           'theming.py',
           'sound.py',
           'browser.py',
           'code_env.py',
           'multimedia.py',
           'web_tools.py',
           'vim.py',
           'shell.py']

HARDWARE = ['power.py']

STEPS = list()
STEPS.extend(MINIMAL)

if INSTALL_ENV == 'machine':
    STEPS.extend(HARDWARE)
