import sys
from cx_Freeze import setup, Executable

# More info <https://github.com/marcelotduarte/cx_Freeze/tree/master/cx_Freeze/samples>
# This script only support py3.7 on MacOS.
# This method at least take 20mb.
# Not good.

build_exe_options = {"packages": ["os"], "excludes": ["sqlite3"],"optimize":2}

base = None

setup(  name = "rimebrew",
        version = "0.3",
        description = "My GUI application!",
        options = {"build_exe": build_exe_options},
        executables = [Executable("importer.py", base=base)])