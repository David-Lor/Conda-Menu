import bullet
from bullet import colors
from shutil import get_terminal_size

from .commands import *
from .messages import *


def _choose(**kwargs):
    """Sub-submenu to choose an existing virtualenv.
    Return the selected virtualenv as a tuple with format (env_name, env_route),
    being env_name the custom virtualenv name, and env_route the absolute path of the env.
    :param envs: List of virtual envs returned by get_envs() (optional, if not available, they will be loaded)
    :param print_loading: if True, print a message while reading the virtual envs (default=False)
    :return: Tuple (env_name, env_route)
    """
    virtualenvs = kwargs.get("envs")
    if not virtualenvs:
        print_loading = kwargs.get("print_loading", False)
        if print_loading:
            print(LOADING_ENVS)
        virtualenvs = get_envs()
        if print_loading:
            clear()
    choices = [e[0] + " (" + e[1] + ")" for e in virtualenvs]
    virtualenvs.append((None, None))
    choices.append(RETURN)
    selection = bullet.ScrollBar(
        prompt=CHOOSE_PROMPT,
        choices=choices,
        height=get_terminal_size((30, 30)).lines - 5,
        word_color=colors.bright(colors.foreground["blue"]),
        word_on_switch=colors.bright(colors.foreground["white"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["green"],
        indent=1,
        margin=2
    ).launch()
    selection_index = choices.index(selection)
    return virtualenvs[selection_index]


# noinspection PyUnusedLocal
def _exit(**kwargs):
    """Quit the application
    """
    clear()
    exit(0)


# noinspection PyUnusedLocal
def _new(**kwargs):
    """Create a new virtualenv, asking for the env name and package/s to install.
    :return: True if a new virtualenv was theorically created; False if not
    """
    clear()
    virtualenv_name = ""
    virtualenv_packages = ""
    virtualenv_no_packages = False
    while not virtualenv_name or (not virtualenv_packages and not virtualenv_no_packages):
        if not virtualenv_name:
            virtualenv_name = input(NAME_PROMPT).strip()
        if not virtualenv_name:
            print(NAME_WARNING)
        elif virtualenv_name == "q":
            return False
        else:
            virtualenv_packages = input(PACKAGES_PROMPT).strip()
            if not virtualenv_packages:
                virtualenv_no_packages = bullet.YesNo(NOPACKAGES_CONFIRM).launch()
    new_env(virtualenv_name, virtualenv_packages)
    return True


def _open(**kwargs):
    """Open (activate) an existing virtual env
    :param: envs
    :param: print_loading
    """
    clear()
    virtualenv_name = _choose(**kwargs)[0]
    if virtualenv_name:
        activate_env(virtualenv_name)


def _delete(**kwargs):
    """Delete an existing virtual env
    :param: envs
    :param: print_loading
    """
    clear()
    virtualenv_name = _choose(**kwargs)[0]
    if virtualenv_name:
        delete_env(virtualenv_name)
    return bool(virtualenv_name)


def _main():
    """Main menu
    """
    existing_envs = get_envs()
    n_existing_envs = len(existing_envs)
    if n_existing_envs > 0:  # Envs available
        choices_txt = [MAIN_OPEN, MAIN_NEW, MAIN_DELETE, EXIT]
        choices_functions = [_open, _new, _delete, _exit]
    else:  # No envs available
        choices_txt = [MAIN_NEW, EXIT]
        choices_functions = [_new, _exit]
    clear()
    cli = bullet.ScrollBar(
        prompt=MAIN_TITLE,
        choices=choices_txt,
        word_color=colors.bright(colors.foreground["blue"]),
        word_on_switch=colors.bright(colors.foreground["white"]),
        background_color=colors.background["black"],
        background_on_switch=colors.background["green"],
        indent=3,
        margin=2
    )
    selection_index = choices_txt.index(cli.launch())
    func = choices_functions[selection_index]
    func(print_loading=True)


def run():
    """Run the main menu on a loop.
    Run the application itself.
    """
    while True:
        try:
            _main()
        except (KeyboardInterrupt, InterruptedError):
            break
    _exit()
