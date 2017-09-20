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
# LISTS

# "Merging" two lists together

names = ["Bob", "Jessica", "Mary", "John", "Mel"]
births = [968, 155, 77, 578, 973]
BabyDataSet = list(zip(names, births))
BabyDataSet
# [('Bob', 968), ('Jessica', 155), ('Mary', 77), ('John', 578), ('Mel', 973)]

####################################################################
#
# DEBUGGING

import pdb
pdb.set_trace()                 # Sets a breakpoint here.


####################################################################
#
# DECORATORS

# This is the actual decorator.
def my_decorator(original_function):
    def new_function(*args, **kwargs):
        print("Preparing to call the function.")
        print("args: " + str(args))
        print("kwargs: " + str(kwargs))
        original_function(*args, **kwargs)
        print("Called the original function.")

    return new_function


# This is an annotation. It prevents hello from being called directly.
# Instead, the decorator (my_decorator) is called, which returns a
# function. THAT function is called, instead of hello.
@my_decorator
def hello(target_name=None):
    if target_name:
        print("Hello, " + target_name + "!")
    else:
        print("Hello, world!")


hello2()
hello2("foo")
                                                                    
####################################################################
#
# COOL TRICKS

# Neat syntax for finding errors:
errors = log_data.filter(lambda line: "ERROR" in line)

