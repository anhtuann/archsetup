INSTALL_ENV = 'machine'
#Real install would be 'machine'

MINIMAL = ['pacaur.py',
           'xserver.py',
           'backlight.py',
           'fonts.py',
           'fs_management.py',
           'sound.py',
           'vim.py',
           'shell.py']

HARDWARE = ['power.py',
            'battery.py',
            'sys_tools.py',
            'input.py',
            'network.py']

CODING = ['web_dev.py',
          'tensorflow.py',
          'android.py']

STEPS = list()
STEPS.extend(MINIMAL)

if INSTALL_ENV == 'machine':
    STEPS.extend(HARDWARE)
    #STEPS.extend(CODING)
