#!/usr/bin/env python3

from os import name, getcwd

var_name = ''

def do_work(var_name):
    if name == 'nt':
        current_cmd_path = getcwd() + '\\' + var_name
    elif name == 'posix':
        current_cmd_path = getcwd() + '/' + var_name
    else:
        print('error, check os.name in get_dir.py')
        return None
    return current_cmd_path
