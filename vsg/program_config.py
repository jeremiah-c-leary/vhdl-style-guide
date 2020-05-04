
import os
import sys
import yaml

sHomeDefaultFile = '~/.config/vhdl-style-guide/config.yaml'
sEnvironmentVariable = 'VSG_DEFAULT_CONFIG'


def update_sys_args():
    '''
    Searches for default configurations and updates the sys.args variable.
    
    Parameters :

    Returns : Nothing 
    '''
    dSysArgs = read_home_program_file()
    dSysArgs = read_environment_variable_program_file(dSysArgs)
    merge_program_config_w_user_sys_args(dSysArgs)


def read_home_program_file():
    '''
    Reads a default configuration in the users home directory it is exists.

    Returns : (dictionary)
    '''
    return open_configuration_file(sHomeDefaultFile, {}, True)


def read_environment_variable_program_file(dSysArgs):
    '''
    Reads a default configuration in the users home directory it is exists.

    Parameters : 

      dSysArgs : (dictionary)

    Returns : (dictionary)
    '''
    try:
        sEnvironmentVariable = os.environ['VSG_DEFAULT_CONFIG']
        return open_configuration_file(sEnvironmentVariable, dSysArgs)
    except KeyError:
        return dSysArgs


def open_configuration_file(sFileName, commandLineArguments, fIgnoreIOerror=False):
    '''Attempts to open a configuration file and read it's contents.'''
    try:
        with open(sFileName) as yaml_file:
            return yaml.full_load(yaml_file)
    except IOError:
        if fIgnoreIOerror:
            return {}
        print('ERROR: Could not find configuration file: ' + sFileName)
        sys.exit(1)
    except yaml.scanner.ScannerError as e:
        print('ERROR: Invalid configuration file: ' + sFileName)
        print(e)
        sys.exit(1)
    except yaml.parser.ParserError as e:
        print('ERROR: Invalid configuration file: ' + sFileName)
        print(e)
        sys.exit(1)


def merge_program_config_w_user_sys_args(dSysArgs):
    if dSysArgs == {}:
        return sys.argv
    lReturn = sys.argv
    for sKey in list(dSysArgs['command_line_arguments'].keys()):
        if '--' + sKey in lReturn:
            continue
        else:
            lReturn.append('--' + sKey)
            lReturn.append(dSysArgs['command_line_arguments'][sKey])
    return lReturn
