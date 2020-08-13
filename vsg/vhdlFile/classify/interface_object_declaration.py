
from vsg.vhdlFile.classify import interface_signal_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    interface_object_declaration ::=
        interface_constant_declaration
      | interface_signal_declaration
      | interface_variable_declaration
      | interface_file_declaration
    '''
    if interface_signal_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True
    return False


def clear_flags(dVars):

    interface_signal_declaration.clear_flags(dVars)
