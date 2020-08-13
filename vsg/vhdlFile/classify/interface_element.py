
from vsg.vhdlFile.classify import interface_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    interface_element ::= interface_declaration
    '''

    if interface_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):

    interface_declaration.clear_flags(dVars)
