import subprocess
from datetime import datetime

from .messages import *


def activate_env(virtualenv_name):
    """Activate an available virtual env.
    The process to activate and interact with the env is:
    - Create a new tmux session on detached mode
    - Send the 'conda activate' command to the tmux session
    - Attach to that session
    :param virtualenv_name: name of the virtual env
    """
    session_name = "condamenu-activated-" + str(int(datetime.now().timestamp())) + "-" + virtualenv_name
    session_name = session_name.replace(".", "")
    subprocess.call(["tmux", "new-session", "-d", "-s", session_name])
    subprocess.call(["tmux", "send-keys", "-t", session_name, "conda activate " + virtualenv_name, "ENTER"])
    subprocess.call(["tmux", "attach", "-t", session_name])


def new_env(virtualenv_name, virtualenv_packages):
    """Create a new virtual env.
    The process to create the new env and interact with Conda is:
    - Create a new tmux session on detached mode
    - Send the 'conda create' command to the tmux session
    - Attach to that session
    :param virtualenv_name: custom name for this env
    :param virtualenv_packages: package/s to install
    """
    session_name = "condamenu-newenv-" + str(int(datetime.now().timestamp())) + "-" + virtualenv_name
    session_name = session_name.replace(".", "")
    subprocess.call(["tmux", "new-session", "-d", "-s", session_name])
    subprocess.call([
        "tmux", "send-keys", "-t", session_name,
        "conda create --name={virtualenv_name} {virtualenv_packages} && exit "
        "|| echo '{press_enter}' && read && exit".format(
            virtualenv_name=virtualenv_name,
            virtualenv_packages=virtualenv_packages,
            press_enter=PRESS_ENTER_EXIT
        ),
        "ENTER"
    ])
    subprocess.call(["tmux", "attach", "-t", session_name])


def delete_env(virtualenv_name):
    """Delete an existing virtual env.
    The process to delete the env and interact with Conda is:
    - Create a new tmux session on detached mode
    - Send the 'conda env remove' command to the tmux session
    - Attach to that session
    :param virtualenv_name: custom name of the env to delete
    """
    session_name = "condamenu-rmenv-" + str(int(datetime.now().timestamp())) + "-" + virtualenv_name
    session_name = session_name.replace(".", "")
    subprocess.call(["tmux", "new-session", "-d", "-s", session_name])
    subprocess.call([
        "tmux", "send-keys", "-t", session_name,
        "conda env remove --name={virtualenv_name} && exit "
        "|| echo '{press_enter}' && read && exit".format(
            virtualenv_name=virtualenv_name,
            press_enter=PRESS_ENTER_EXIT
        ),
        "ENTER"
    ])
    subprocess.call(["tmux", "attach", "-t", session_name])


def clear():
    """Clear screen
    """
    subprocess.call(["clear"])


def get_envs():
    """Get available virtual envs.
    Return a list of tuples. Each tuple is a virtual env. Tuple format: (name, route),
    being name the custom name of the virtual env, and route the absolute path of the env.
    :return: List of Tuple (name, route)
    """
    output = subprocess.check_output(["conda", "env", "list"]).decode()
    envs = list()
    for line in output.splitlines():
        if line and not line.startswith('#'):
            line = line.split()
            name = line[0]
            route = line[-1]
            if name not in [env[0] for env in envs]:
                # Avoid duplicates due to a conda bug on "conda env list", when using miniconda
                envs.append((name, route))
    return envs
