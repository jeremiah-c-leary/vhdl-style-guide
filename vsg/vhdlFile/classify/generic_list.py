
from vsg.vhdlFile.classify import interface_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    generic_list ::= *generic*_interface_list
    '''

    if interface_list.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    interface_list.clear_flags(dVars)
