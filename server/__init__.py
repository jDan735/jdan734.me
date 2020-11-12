from os import listdir

files = listdir("server")
__all__ = []

for file in files:
    if file.endswith(".py") and not file == "__init__.py":
        __all__.append(file[:-3])
