from typing import List
from enum import Enum
import os
import sys
import sysconfig
import ctypes
import itertools

class Platform(Enum):
    LINUX = "linux"
    MACOS = "macos"
    WINDOWS = "windows"

def __get_platform() -> Platform:
    """
    Get the platform type.
    """
    if sys.platform.startswith("linux"):
        return Platform.LINUX
    elif sys.platform.startswith("darwin"):
        return Platform.MACOS
    elif sys.platform.startswith("win32"):
        return Platform.WINDOWS
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

def __get_library_filename(name: str) -> str:
    platform = __get_platform()
    if platform == Platform.LINUX:
        return f"lib{name}.so"
    elif platform == Platform.MACOS:
        return f"lib{name}.dylib"
    elif platform == Platform.WINDOWS:
        return f"{name}.dll"

def __get_library_directory_names() -> List[str]:
    """
    Get the library directory names based on the platform.
    """
    platform = __get_platform()
    if platform == Platform.LINUX:
        return ["lib", "lib64"]
    elif platform == Platform.MACOS:
        return ["lib"]
    elif platform == Platform.WINDOWS:
        return ["Lib", "libs"]

def __get_directory_prefixes() -> List[str]:
    """
    Get the prefixes for the library search paths.
    """
    return [sys.prefix]

def __load_library(name: str) -> ctypes.CDLL:
    """
    Heuristically find and load a library with the specified name.
    """
    filename = __get_library_filename(name)
    try:
        return ctypes.CDLL(filename)
    except OSError:
        pass

    prefixes = __get_directory_prefixes()
    lib_directories = __get_library_directory_names()
    for prefix, lib_directory in itertools.product(prefixes, lib_directories):
        path = os.path.join(prefix, lib_directory, filename)
        if os.path.exists(path):
            try:
                return ctypes.CDLL(path)
            except OSError:
                continue
    
    raise OSError(f"Could not find {name}")

def load_core() -> ctypes.CDLL:
    """
    Load the core library for xmipp4.
    
    This function attempts to load the xmipp4 shared object from the system's
    library directories. It raises an exception if the library cannot be found.
    
    Returns:
        ctypes.CDLL: The loaded core library.
    """
    return __load_library("xmipp4-core")
