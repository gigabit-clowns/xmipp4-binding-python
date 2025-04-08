import ctypes
import os
import platform
import sys
from typing import List

def __get_library_filename(name: str, system: str) -> str:
    """Get the library filename based on the operating system."""
    if system == 'Darwin':
        return f"lib{name}.dylib"
    elif system == 'Windows':
        return f"{name}.dll"
    else: # Linux or other Unix-like systems
        return f"lib{name}.so"

def __get_library_directory_names(system) -> List[str]:
    """Get the library directory names based on the operating system."""
    if system == 'Windows':
        return ["bin"]
    else: # Linux, MacOS, or other Unix-like systems
        return ["lib", "lib64"]

def __load_library(name: str) -> ctypes.CDLL:
    """Heuristically find and load a library with the specified name."""
    system = platform.system()
    filename = __get_library_filename(name, system)
    possible_paths = [
        filename,
        *[
            os.path.join(sys.prefix, lib_directory, filename)
            for lib_directory in __get_library_directory_names(system)
        ]
    ]

    for path in possible_paths:
        if os.path.exists(path):
            try:
                return ctypes.CDLL(path)
            except OSError:
                continue
    
    raise OSError(f"Could not find {name}.")

def load_core() -> ctypes.CDLL:
    """
    Load the core library for xmipp4.
    
    This function attempts to load the xmipp4 shared object from the system's
    library directories. It raises an exception if the library cannot be found.
    
    Returns:
        ctypes.CDLL: The loaded core library.
    """
    return __load_library("xmipp4-core")
