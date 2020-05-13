
import glob
import os
import sys
import yaml

sHomeDefaultFile = os.path.expanduser('~/.config/vhdl-style-guide/config.yaml')
sEnvironmentVariable = 'VSG_DEFAULT_CONFIG'


def update_sys_args():
    '''
    Searches for default configurations and updates the sys.args variable.
    
    Parameters :

    Returns : Nothing 
    '''
    dSysArgs = read_home_program_file()
    dSysArgs = read_environment_variable_program_file(dSysArgs)
    remove_unsupported_arguments(dSysArgs)
    expand_environment_vars(dSysArgs)
    glob_files(dSysArgs)
    convert_single_dash_argument_to_double_dash_argument()
    merge_program_config_w_user_sys_args(dSysArgs)


def read_home_program_file():
    '''
    Reads a default configuration in the users home directory it is exists.

    Returns : (dictionary)
    '''
    dTemp = open_configuration_file(sHomeDefaultFile, {}, True)
    return dTemp


def read_environment_variable_program_file(dSysArgs):
    '''
    Reads a default configuration in the users home directory it is exists.

    Parameters : 

      dSysArgs : (dictionary)

    Returns : (dictionary)
    '''
    try:
        sEnvironmentVariable = os.path.expanduser(os.path.expandvars(os.environ['VSG_DEFAULT_CONFIG']))
        return open_configuration_file(sEnvironmentVariable, dSysArgs)
    except KeyError:
        return dSysArgs


def remove_unsupported_arguments(dSysArgs):
    '''
    Removes the following keys from the dictionary:

       output_configuration
       help
       version
       rule_configuration

    Parameters :

        dSysArgs : (dictionary)

    Returns : nothing
    '''
    if dSysArgs == {}:
        return
    lRemovedKeys = ['output_configuration', 'help', 'version', 'rule_configuration']
    for sKey in list(dSysArgs['command_line_arguments'].keys()):
        if sKey in lRemovedKeys:
            del dSysArgs['command_line_arguments'][sKey] 


def convert_single_dash_argument_to_double_dash_argument():
    '''
     Converts sys.argv single dash arguments to double dash arguments.
    '''

    for iIndex, sArg in enumerate(sys.argv):
        if sArg == '-f':
            sys.argv[iIndex] = '--filename'
        elif sArg == '-lr':
            sys.argv[iIndex] = '--local_rules'
        elif sArg == '-c':
            sys.argv[iIndex] = '--configuration'
        elif sArg == '-fp':
            sys.argv[iIndex] = '--fix_phase'
        elif sArg == '-j':
            sys.argv[iIndex] = '--junit'
        elif sArg == '-of':
            sys.argv[iIndex] = '--output_format'
        elif sArg == '-b':
            sys.argv[iIndex] = '--backup'


def open_configuration_file(sFileName, commandLineArguments, fIgnoreIOerror=False):
    '''Attempts to open a configuration file and read it's contents.'''
    try:
        with open(sFileName) as yaml_file:
            oTemp = yaml.full_load(yaml_file)
            return oTemp
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
    '''
    Combines the program configuration with the user supplied command line arguments.

    Parameters :

        dSysArgs : (dictionary)

    Returns : (list of strings)
    '''
    if dSysArgs == {}:
        return sys.argv
    lReturn = sys.argv
    for sKey in list(dSysArgs['command_line_arguments'].keys()):
        if '--' + sKey in lReturn:
            continue
        else:
            paramValue = extract_parameter_value(dSysArgs, sKey)
            if paramValue == False:
               continue
            lReturn.append('--' + sKey)
            if not paramValue == True:
                lReturn.extend(convert_param_to_list(paramValue))
    return lReturn


def convert_param_to_list(param):
    '''
    Converts a single entry parameter into a list.

    Parameters :

        param : (string or list)

    Returns : (list)
    '''
    if isinstance(param, list):
        return param
    elif isinstance(param, int):
        return [str(param)]
    else:
        return [param]


def extract_parameter_value(dSysArgs, sKey):
    '''
    Returns the key value of the provided key.
    
    Parameters :

        dSysArgs : (dictionary)

        sKey : (string)

    Returns : (string or list)
    '''
    return dSysArgs['command_line_arguments'][sKey]


def expand_environment_vars(dSysArgs):
    '''
    Expands environment variables in filenames.

    Parameters : 

        dSysArgs: (dictionary)

    Returns : (dictionary)

    '''

    try:
        lUpdates = []
        for sFilename in dSysArgs['command_line_arguments']['filename']:
            lUpdates.append(os.path.expanduser(os.path.expandvars(sFilename)))
        dSysArgs['command_line_arguments']['filename'] = lUpdates
    except KeyError:
      pass

    try:
        lUpdates = []
        for sFilename in dSysArgs['command_line_arguments']['configuration']:
            lUpdates.append(os.path.expanduser(os.path.expandvars(sFilename)))
        dSysArgs['command_line_arguments']['configuration'] = lUpdates
    except KeyError:
      pass

    try:
        dSysArgs['command_line_arguments']['junit'] = os.path.expanduser(os.path.expandvars(dSysArgs['command_line_arguments']['junit']))
    except KeyError:
      pass

    try:
        dSysArgs['command_line_arguments']['local_rules'] = os.path.expanduser(os.path.expandvars(dSysArgs['command_line_arguments']['local_rules']))
    except KeyError:
      pass

    return dSysArgs


def glob_files(dSysArgs):
    '''
    Expands * in filenames.

    Parameters :

        dSysArgs : (dictionary)

    Returns : (dictionary)
    '''
    try:
        lUpdates = []
        for sFilename in dSysArgs['command_line_arguments']['filename']:
            lUpdates.extend(glob.glob(sFilename))
        dSysArgs['command_line_arguments']['filename'] = lUpdates
    except KeyError:
      pass

    try:
        lUpdates = []
        for sFilename in dSysArgs['command_line_arguments']['configuration']:
            lUpdates.extend(glob.glob(sFilename))
        dSysArgs['command_line_arguments']['configuration'] = lUpdates
    except KeyError:
      pass

    return dSysArgs
