import ctypes
import pathlib

if __name__ == "__main__":
    libname = pathlib.Path().absolute() / "Dll/libLab1.dll"

    c_lib = ctypes.CDLL(str(libname))
