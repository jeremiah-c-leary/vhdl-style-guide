
from vsg.vhdlFile.classify import interface_object_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    interface_declaration ::=
        interface_object_declaration
      | interface_type_declaration
      | interface_subprogram_declaration
      | interface_package_declaration
    '''

    if interface_object_declaration.tokenize(oObject, iObject, lObjects, dVars):
         return True

    return False


def clear_flags(dVars):

    interface_object_declaration.clear_flags(dVars)
