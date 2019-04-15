# Conda/Miniconda Menu

A console menu to manage your Conda virtual envs: create new envs, view created envs, activate an env, delete an env. Menus made with [bullet](https://github.com/Mckinsey666/bullet). Working (tested) on Linux only.

## Installing

```bash
git clone https://github.com/David-Lor/Conda-Menu.git
cd Conda-Menu
python setup.py install
```

## Requirements

- Python 3.x (tested on 3.7)
- tmux installed on the system (available on repositories of most of the available Linux distros)
- Conda/Miniconda installed and working, obviously
- [bullet](https://github.com/Mckinsey666/bullet) (auto-installed by setup.py)

## Usage

Once installed:

```bash
condamenu
```

Or you can run directly without installing it:

```bash
git clone https://github.com/David-Lor/Conda-Menu.git
python Conda-Menu
```

## Set menu language

For now, the application is displayed on English or Spanish. It uses the system locale to determine the language, being English the default language.

If your system locale is set to "es_xx" but you want to force it to be in English, or your locale is not "es_xx", you can force it by setting a system env variable called "CONDAMENU_LANG", with the value "es" to set it to Spanish, or any other value to set it to the default language (English).

## How does it work?

The application call for conda commands (using subprocess lib) to list virtual envs, create or remove them.
Whenever an interactive prompt is required (when creating, removing or activating a virtual env), a new Tmux session is created and attached to.

## Changelog

- 1.0.0 - Initial release
- 1.0.1 - Avoid duplicates on virtual env choosing sub-menu, due to a "conda env list" bug when using miniconda
- 1.0.2 - Avoid invalid names on Tmux sessions when a virtual env name contains a dot ('.')

## TODO

- Recycle the list of existing virtual envs across the functions that require them, saving a few ms of loading between sub-menus
- Option to massive-remove envs
- Add hotkeys
