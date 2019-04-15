from os import getenv
from locale import getdefaultlocale

locale = getdefaultlocale()[0]
env_lang = getenv("CONDAMENU_LANG", "")


# ES strings
if locale.startswith("es_") or env_lang.lower() == "es":
    MAIN_TITLE = "\nGestión de entornos virtuales Conda\n"
    MAIN_OPEN = "Abrir un entorno virtual"
    MAIN_NEW = "Crear nuevo entorno virtual"
    MAIN_DELETE = "Eliminar un entorno virtual"
    EXIT = "Salir"
    RETURN = "Volver"
    CHOOSE_PROMPT = "\nSelecciona un entorno virtual:\n"
    NAME_PROMPT = "Nombre del entorno virtual (q para cancelar): "
    NAME_WARNING = "El entorno virtual debe tener un nombre"
    PACKAGES_PROMPT = "Paquetes del entorno virtual (opcional): "
    NOPACKAGES_CONFIRM = "¿Seguro que no quieres añadir paquetes a este entorno virtual?"
    PRESS_ENTER_EXIT = "Pulsa Enter para salir"
    LOADING_ENVS = "Cargando entornos virtuales..."

# ENG strings (default)
else:
    MAIN_TITLE = "\nConda virtual env management\n"
    MAIN_OPEN = "Open a virtual env"
    MAIN_NEW = "Create a new virtual env"
    MAIN_DELETE = "Delete a virtual env"
    EXIT = "Exit"
    RETURN = "Return"
    CHOOSE_PROMPT = "\nChoose a virtual env:\n"
    NAME_PROMPT = "Virtual env name (q to return): "
    NAME_WARNING = "Virtual env must have a name"
    PACKAGES_PROMPT = "Virtual env packages (optional): "
    NOPACKAGES_CONFIRM = "Are you sure you want to create this virtual env without packages?"
    PRESS_ENTER_EXIT = "Press Enter to exit"
    LOADING_ENVS = "Loading virtual envs..."
