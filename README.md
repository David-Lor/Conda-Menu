# Conda/Miniconda Menu

A console menu to manage your Conda virtual envs: create new envs, view created envs, activate an env, delete an env. Menus made with [bullet](https://github.com/Mckinsey666/bullet). Working (tested) on Linux only.

## Installing

```bash
git clone https://github.com/Pythoneiro/Conda-Menu.git
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
git clone https://github.com/Pythoneiro/Conda-Menu.git
python Conda-Menu
```

## How does it work?

The application call for conda commands (using subprocess lib) to list virtual envs, create or remove them.
Whenever an interactive prompt is required (when creating, removing or activating a virtual env), a new Tmux session is created and attached to.
