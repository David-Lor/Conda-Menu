from setuptools import setup

setup(
    name="condamenu",
    version="1.0.1",
    author="David Lorenzo",
    description="A terminal menu to manage Conda/Miniconda virtual envs",
    long_description="A console menu to manage your Conda virtual envs: "
                     "create new envs, view created envs, activate an env, delete an env. "
                     "Menus made with bullet (https://github.com/Mckinsey666/bullet). Working (tested) on Linux only.",
    url="https://github.com/David-Lor/Conda-Menu",
    packages=["conda_menu"],
    install_requires=["bullet"],
    entry_points={
        'console_scripts': ['condamenu=conda_menu:run'],
    }
)
