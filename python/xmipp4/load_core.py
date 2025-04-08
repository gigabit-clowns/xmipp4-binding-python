from typing import List, Set
from enum import Enum
import os
import sys
import ctypes

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

def __get_library_filename(name: str, platform: Platform) -> str:
    if platform == Platform.LINUX:
        return f"lib{name}.so"
    elif platform == Platform.MACOS:
        return f"lib{name}.dylib"
    elif platform == Platform.WINDOWS:
        return f"{name}.dll"

def __get_library_directory_names(platform: Platform) -> List[str]:
    """
    Get the library directory names based on the platform.
    """
    if platform == Platform.LINUX:
        return ["lib", "lib64"]
    elif platform == Platform.MACOS:
        return ["lib"]
    elif platform == Platform.WINDOWS:
        return ["bin"]

def __load_library(name: str) -> ctypes.CDLL:
    """
    Heuristically find and load a library with the specified name.
    """
    platform = __get_platform()
    filename = __get_library_filename(name, platform)
    try:
        return ctypes.CDLL(filename)
    except OSError:
        pass

    prefix = sys.prefix
    lib_directories = __get_library_directory_names(platform)
    for lib_directory in lib_directories:
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
