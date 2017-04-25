"""
Requires Python 3.x
Usage: 
 Terminal: (In this example, the terminal prompt is represented by $) 
    Navigate to directory containing get_path.py or type the full path after the python interpreter identifier.
    $ cd <path to get_path.py>
    $ python3 get_path.py <path> <dir> <options>
 
For The Imaging Collective, set of functions which can receive a set of commands either from a file or from terminal
and parse them to separate the command components.
Command components can include:
 - modules to be executed
 - path of data for the module, paths are validated.
 - command line switches
Performs exception handling on commands, calls upon appropriate function based on the command line arguments.
"""
import os
import platform
import time
import sys
from pprint import pprint

_COUNT = 0
_DEBUG = False


def dp(*arg):
    """
    Custom print function for debugging. Iterates through (arg), prints each element in easy to distinguish
    manner.
    
    :param arg:
    :return: None
    """
    global _COUNT
    _COUNT += 1
    print('.'*5, 'Start', '_COUNT')
    for i in arg:
        print(i)
    print('.'*5, 'END', '_COUNT')

def documentation():
    print("Accepts an input")

def inputs(file_arg):
    """
    Parses the command parameters given, separates and passes them to relevant functions.
    
    :param arg:list(str): file_arg:
    :return: final_path_arg : the part of command containing information for the path to be used for subsequent
    operations.
    """
    global _DEBUG
    if len(file_arg) == 0:
        print()
        print("ERROR. Command parameters not registered!")
        print("Source Code debugging might be necessary.")
        print("Contact the program author. Include a screenshot and details of the error if possible.")
        print("Terminating program...")
        quit()
    elif len(file_arg) == 1:  # when no path or switches used, and executed command is the only arg.
        final_path_arg = os.getcwd()
    elif len(file_arg) > 1:
        if file_arg[1][0] == '-':  # when path not specified but switches used.
            final_path_arg = os.getcwd()
        else:
            final_path_arg = file_arg[1]
    if '--debug' in file_arg:
        _DEBUG = True
    if '--help' or '-h' in file_arg:
        print(__doc__)
    return final_path_arg
         

def paths(final_path_arg):
    """
    Gets the inputs given as terminal parameters and processes them.
    Functions:
        - Path construction
        - Path resolution and conversion between nix and nt systems.
        - Path Verification for existence.
        - Path related exception handling.
        
    :param arg: final_path_arg: part of the command containing the path information.
    :return: path_ :  The final path to be used in subsequent operations.
    """
    global _DEBUG
    path_ = os.path.realpath(os.path.expanduser(final_path_arg))
    if os.path.exists(path_) is False:
        print("ERROR. Specified path does not exist.")
        print('Interpreted path:', path_)
        if _DEBUG is True:
            print("Continuing testing without terminating program.")
        else:
            print("Terminating program...")
            quit()
    else:
        return path_
    
    
def run_from_file(data_file):
    """
    Accepts a file with (multiple) command(s) in leu of individual commands given by the user from the terminal CLI.
    Useful for batch processing and testing. Parses each listed command and passes it on to appropriate functions.
    :param arg: str, data_file: path to text file
    :return:
    """
    # in nt (windows) systems, replaces \t in paths with \\t, preventing its interpretation as tab character.
    if os.name == 'nt':
        data_file = data_file.replace('\t', '\\t')
    print(os.path.realpath(data_file))
    with open(data_file, 'r') as f_obj:
        file_args = f_obj.read()
        file_args = file_args.splitlines()
    for file_arg_ in file_args:
        print()
        # print('Input -- test().file_arg_:  ', file_arg_)
        str2argv = file_arg_.split(sep=' ')
        use(str2argv)
        
        
def run_from_terminal():
    """
    Accepts a CLI command and passes it on to the appropriate functions.
    :params: None
    :return:
    """
    file_arg_ = sys.argv
    use(file_arg_)
        

def use(file_args):
    """
    Accepts individual command and passes it onto and around to appropriate functions.
    :param arg: list(str), file_args:
    :return: path_
    """
    global _DEBUG
    resolved_inputs = inputs(file_args)
    path_ = paths(resolved_inputs)
    if _DEBUG is True:
        print('Input  -- ', file_args)
        print('Output -- ', path_)
    return path_

    
def main(data_file):
    global _DEBUG
    if os.name == 'nt':
        _DEBUG = True
        run_from_file(data_file)
    else:
        _DEBUG = False
        run_from_terminal()
    

if __name__ == '__main__':
    print()
    test_data_file = os.path.join(os.getcwd(), os.path.relpath("tests/data/test_paths_from_sh.txt"))
    main(test_data_file)
    





