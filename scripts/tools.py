import subprocess
import contextlib
import os
import glob

def bash_cmd(args, shell=False):
    print(' '.join(args))
    if not shell:
        subprocess.run(args, stdout=subprocess.PIPE)
    else:
        arguments = ' '.join(args)
        subprocess.run(arguments, stdout=subprocess.PIPE, shell=True)

def pacman(packages, makepkg=False, noconfirm=True):
    command = ['sudo', 'pacman']
    if not makepkg:
        command.append('-S')
    else:
        command.append('-U')
    if noconfirm:
        command.append('--noconfirm')
    for package in packages:
        command.append(package)
    bash_cmd(args = command)

def pacaur(packages, makepkg=False, noconfirm=True):
    command = ['pacaur']
    if not makepkg:
        command.append('-S')
    else:
        command.append('-U')
    if noconfirm:
        command.append('--noconfirm')
    for package in packages:
        command.append(package)
    bash_cmd(args = command)

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
        command.append(custom_path)
    bash_cmd(args = command)

def makepkg(package):
    bash_cmd(['makepkg', '-s'])
    pacman(glob.glob(package), makepkg=True)

def mkdir(path):
    bash_cmd(['mkdir', '-p', path])

def link_conf(source, link, sudo = False):
    # need shell True to use tilde wildcard in symlinks
    command = ['sudo', 'ln', '-s', source, link]
    if sudo == False:
        bash_cmd(command[1:], shell=True)
    else:
        bash_cmd(command, shell=True)
