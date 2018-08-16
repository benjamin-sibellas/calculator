application_title = "My calculator" 
main_python_file = "calculator.py"

import sys

from cx_Freeze import setup, Executable

setup(
    name = application_title,
    version = "1.0",
    description = "My calculator",
    executables = [Executable(main_python_file)]
)