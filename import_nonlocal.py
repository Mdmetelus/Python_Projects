# import from another folder

# some_file.py
import sys
sys.path.insert(0, '/path/to/application/app/folder')

import file

folders require to have __init__.py

its messy, much easier to keep everything in one place

# https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html#case-4-importing-from-parent-directory