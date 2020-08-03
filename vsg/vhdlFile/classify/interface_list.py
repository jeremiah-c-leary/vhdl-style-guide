
from vsg.token import interface_list as token
from vsg.vhdlFile.classify import interface_signal_declaration

def interface_list(oObject, iObject, lObjects, dVars):
    '''
    Classifies signal interface declarations:

    [ signal ] identifier_list : [ mode ] subtype_indication [ bus ] [ := static_expression ] ;

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

    classify_interface_declaration(oObject, iObject, lObjects, dVars)


def classify_interface_declaration(oObject, iObject, lObjects, dVars):

    classify_interface_object_declaration(oObject, iObject, lObjects, dVars)


def classify_interface_object_declaration(oObject, iObject, lObjects, dVars):

    interface_signal_declaration.interface_signal_declaration(oObject, iObject, lObjects, dVars)

def clear_flags(dVars):

    interface_signal_declaration.clear_flags(dVars)
