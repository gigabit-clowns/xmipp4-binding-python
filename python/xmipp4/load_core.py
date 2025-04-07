import os
import sys
import ctypes

def __get_library_filename(name: str) -> str:
    if sys.platform.startswith("linux"):
        return f"lib{name}.so"
    elif sys.platform.startswith("darwin"):
        return f"lib{name}.dylib"
    elif sys.platform.startswith("win32"):
        return f"{name}.dll"
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

def load_core() -> ctypes.CDLL:
    """
    Load the core shared object of xmipp4.
    """
    
    paths = [
        os.path.join(sys.prefix, "lib"),
        os.path.join(sys.prefix, "lib64"),
    ]
    
    filename = __get_library_filename("xmipp4-core")
    for path in paths:
        full_path = os.path.join(path, filename)
        if os.path.exists(full_path):
            return ctypes.CDLL(full_path)
        
    return ctypes.CDLL(filename)
