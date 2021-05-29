import os
import sys
import schoola
import schoola.settings
import schoola.persistence


def set_debug():
    schoola.settings.DEBUG = True


# Activate v env according to different operating systems.
def _get_venv_activation_command():
    #  missing you all the time posix :( hold on, i'll come back to you .
    if os.name == 'posix':
        return ' '.join(['source', os.path.join('.venv', 'bin', 'activate')])
    elif os.name == 'nt':
        return os.path.join('.venv', 'Scripts', 'activate')
    return None

#  Check whether the path of v env and the directory itself exist or not.
#  If they are there, do nothing.
#  If they are not, then generate v env for appropriate operating system.
def init_venv():
    if os.path.exists('.venv') and os.path.isdir('.venv'):
        return
    if os.name == 'posix':
        os.system('virtualenv .venv -p python3')
    elif os.name == 'nt':
        os.system('python -m virtualenv .venv -p python3')
    else:
        print('Unknown OS name.')


#  Check all required packages have to set in v env, if packages are already exist, do nothing
#  check that 'is v env has been activated?' if it has not, activate it by activation function.
#  After all these successfully passed processes; read the  text file and install all the package file has.
def install_deps():
    if not os.path.exists('requirements.txt'):
        return
    venv_activation_command = _get_venv_activation_command()
    if not venv_activation_command:
        print('Unknown OS name.')
        return
    os.system(f'{venv_activation_command} && pip install -r requirements.txt')


#  Activate v env and write all the dependencies to the requirements text file.
def lock_deps():
    venv_activation_command = _get_venv_activation_command()
    if not venv_activation_command:
        print('Unknown OS name.')
        return
    os.system(f'{venv_activation_command} && pip freeze > requirements.txt')


#  Migrate all when db changes.
def migrate_db():
    schoola.persistence.Database.migrate()

def start_server():
    server = schoola.Server()
    server.start()

#  It works as if 'this command' then do 'this'.
COMMANDS = {
    '--debug': set_debug,
    'venv.init': init_venv,
    'deps.install': install_deps,
    'deps.lock': lock_deps,
    'db.migrate': migrate_db,
    'server.start': start_server
}


#  It checks for all variables entered to the terminal by developer,
#  except the first argument.
#  It prints out custom error if it doesn't contain any of given Commands keys,
#  otherwise it runs the function of each variable.
def main(args):
    for arg in args[1:]:
        if arg not in COMMANDS:
            print(f'Unknown command: {arg}')
            return
        COMMANDS[arg]()
        if not arg.startswith('--'):
            return


#  For running program by its name and taking all variables from cmd.
if __name__ == '__main__':
    main(sys.argv)


