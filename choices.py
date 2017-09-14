INSTALL_ENV = 'machine'
#Real install would be 'machine'

MINIMAL = ['pacaur.py',
           'cli_tools.py',
           'xserver.py',
           'backlight.py',
           'i3wm.py',
           'fs_management.py',
           'fonts.py',
           'theming.py',
           'sound.py',
           'browser.py',
           'code_env.py',
           'web_dev.py',
           'multimedia.py',
           'web_tools.py',
           'office.py',
           'vim.py',
           'shell.py']

HARDWARE = ['power.py',
            'sys_tools.py',
            'input.py',
            'network.py']

STEPS = list()
STEPS.extend(MINIMAL)

if INSTALL_ENV == 'machine':
    STEPS.extend(HARDWARE)
