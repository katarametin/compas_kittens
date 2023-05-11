import os

from compas.plugins import plugin
from compas_ghpython.components import install_userobjects


@plugin(category="install")
def installable_rhino_packages():
    return ["compas_kittens"]


@plugin(category="install")
def after_rhino_install(installed_packages):
    import compas_kittens

    install_folder = os.path.dirname(compas_kittens.__file__)
    userobjects = os.path.join(install_folder, "ghpython", "components", "ghuser")

    installed_objects = install_userobjects(userobjects)

    return [
        (
            "compas_kittens",
            "Installed {} GH User Objects".format(len(installed_objects)),
            True,
        )
    ]
