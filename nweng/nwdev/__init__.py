from typing import cast, Type
import importlib
from nweng.nwdev.api import API
from nweng.nwdev.api.api import APIImple

def NwDev() -> API:
    type_fqn = get_fqn(APIImple)
    api = get_class(type_fqn, API)
    return api


def dynamic_import(module_name):
    try:
        module = importlib.import_module(module_name)
        #print(f"Module {module_name} imported successfully.")
        return module
    except ImportError:
        print(f"Module {module_name} not found.")
        return None

def get_class(fqn: str, type: API) -> API:
    """Given a fully qualifed class name, import the module and return the class"""
    module_name, class_name = fqn.rsplit(".", 1)
    module = dynamic_import(module_name)
    cls = getattr(module, class_name)
    return cast(API, cls)

def get_fqn(cls: Type[object]) -> str:
    """Given a class, return its fully qualified name"""
    return f"{cls.__module__}.{cls.__name__}"