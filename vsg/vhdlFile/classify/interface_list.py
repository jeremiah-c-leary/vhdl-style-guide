
from vsg.token import interface_list as token
from vsg.vhdlFile.classify import interface_signal_declaration

def interface_list(oObject, iObject, lObjects, dVars):
    '''
    Classifies interface_lists

    interface_list ::= interface_element { ; interface_element }

    '''
    if classify_semicolon(oObject, iObject, lObjects, dVars):
        return
    else:
        classify_interface_element(oObject, iObject, lObjects, dVars)
            

def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        interface_signal_declaration.clear_flags(dVars)


def classify_interface_element(oObject, iObject, lObjects, dVars):
    '''
    interface_element ::= interface_declaration
    '''

    classify_interface_declaration(oObject, iObject, lObjects, dVars)


def classify_interface_declaration(oObject, iObject, lObjects, dVars):
    '''
    interface_declaration ::=
        interface_object_declaration
      | interface_type_declaration
      | interface_subprogram_declaration
      | interface_package_declaration
    '''

    classify_interface_object_declaration(oObject, iObject, lObjects, dVars)


def classify_interface_object_declaration(oObject, iObject, lObjects, dVars):
    '''
    interface_object_declaration ::=
        interface_constant_declaration
      | interface_signal_declaration
      | interface_variable_declaration
      | interface_file_declaration
    '''
    interface_signal_declaration.interface_signal_declaration(oObject, iObject, lObjects, dVars)


def clear_flags(dVars):

    interface_signal_declaration.clear_flags(dVars)
