import subprocess
import contextlib
import os
import glob

def bash_cmd(cmd):
    '''
    Arguments :
        cmd (str)

    execute the command cmd
    '''
    print(cmd)
    subprocess.run(cmd, shell=True)

def pacman(packages, makepkg=False, noconfirm=True):
    command = ['sudo -v', 'pacman']
    if not makepkg:
        command.append('-S')
    else:
        command.append('-U')
    if noconfirm:
        command.append('--noconfirm')
    command.append('--needed')
    for package in packages:
        command.append(package)
    bash_cmd(' '.join(command))

def pacaur(packages, makepkg=False, noconfirm=True):
    command = ['pacaur']
    if not makepkg:
        command.append('-S')
    else:
        command.append('-U')
    if noconfirm:
        command.append('--noconfirm')
    command.append('--needed')
    for package in packages:
        command.append(package)
    bash_cmd(' '.join(command))

@contextlib.contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def git_clone(repository, custom_path = 'Nope'):
    command = ['git', 'clone']
    command.append(repository)
    if custom_path != 'Nope':
        command.append(os.path.expanduser(custom_path))
    bash_cmd(' '.join(command))

def makepkg(package):
    bash_cmd('makepkg -s')
    pacman(glob.glob(package), makepkg=True)

def mkdir(path, sudo = False):
    command = 'mkdir -p {}'.format(os.path.expanduser(path))
    if sudo == True:
        sudo_cmd = 'sudo -v ' + command
        bash_cmd(sudo_cmd)
    else:
        bash_cmd(command)

def stow(package, source='~/.dotfiles/', sudo=False):
    if sudo is False:
        bash_cmd('stow -v -d {} -t ~ {}'.format(source, package))
    else:
        bash_cmd('sudo -v stow -v -d {} -t / {}'.format(source, package))

def link_conf(source, link, sudo = False):
    command = ['sudo -v', 'ln', '-sf', os.path.expanduser(source), os.path.expanduser(link)]
    if not sudo:
        bash_cmd(' '.join(command[1:]))
    else:
        bash_cmd(' '.join(command))
