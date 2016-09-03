#!/usr/bin/env python3

####################################################################
#
# PACKAGES
#
# Packages are a special type of module. Can contain other modules,
# including other packages. Example:
#
# Package
# - Module
# - Package
#   - Module
#
# Packages are typically directories (and have a
# package_name.__path__), while modules are typically single files.
#
# sys.path tells Python where to look for modules.
#
# If you start Python with no args, then sys.path[0] == '', which
# means the current directory.


####################################################################
#
# DEBUGGING

import pdb
pdb.set_trace()                 # Sets a breakpoint here.
