"""Methods to see what functions/symbols are part of an imported module/package"""

# Check which functions have been imported.
# import sys
# from inspect import getmembers, isfunction
# from pathlib import Path
# functions_list = getmembers(sys.modules['pathlib'], isfunction)
# print(functions_list)
# print(dir(Path))
# print(help(Path))

# Check which symbols have been imported.
symbols_before = dir()
print(f"before: {symbols_before}")
# import pathlib
from pathlib import Path
symbols_after = dir()
print(f"after: {symbols_after}")
imported_symbols = [s for s in symbols_after if not s in symbols_before]
print(f"imported: {imported_symbols}")
