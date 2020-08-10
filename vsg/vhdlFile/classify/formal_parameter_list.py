
from vsg.vhdlFile.classify import interface_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    formal_parameter_list ::= *parameter*_interface_list
    '''
    if interface_list.interface_list(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    interface_list.clear_flags(dVars)
