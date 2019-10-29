#!/usr/bin/env python3

from os import name, getcwd

# When defining function, specify that the 
# parameter should be of string type when called
# from user programs.
def get_os_dir_append_name(a_file_name: str):
    # The next triple double-quote block specifies
    # A description for this program function.
    # Anyone can read this 'documentation string'
    # by print(get_os_dir_append_name.__doc__)
    """
    Automatically find your current working directory
    in your terminal session.
    Optionally reference A file name string for directory. 
    """
    if name == 'nt':
        current_cmd_path = getcwd() + '\\' + a_file_name
    elif name == 'posix':
        current_cmd_path = getcwd() + '/' + a_file_name
    else:
        print('error, check os.name in get_dir.py')
        return None
    return current_cmd_path
