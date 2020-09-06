
from vsg.token import interface_signal_declaration as token
from vsg import parser

lModes = ['in', 'out', 'inout', 'buffer', 'linkage']


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    Classifies signal interface declarations:

    [ signal ] identifier_list : [ mode ] subtype_indication [ bus ] [ := static_expression ] ;

    '''
    if not dVars['bInterfaceSignalDeclarationColonFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

        if classify_comma(oObject, iObject, lObjects, dVars):
            return True 

        if classify_colon(oObject, iObject, lObjects, dVars):
            return True 

        if classify_identifier(oObject, iObject, lObjects, dVars):
            return True 

    else:
        if not dVars['bInterfaceSignalDeclarationAssignmentOperatorFound']:

            if classify_assignment_operator(oObject, iObject, lObjects, dVars):
                return True

            if classify_subtype_indication(oObject, iObject, lObjects, dVars):
                return True 

            if classify_mode_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_bus_keyword(oObject, iObject, lObjects, dVars):
                return True 

        else:

            if classify_static_expression(oObject, iObject, lObjects, dVars):
                return True 


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'signal':
        lObjects[iObject] = token.signal_keyword(sValue)
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item and sValue != ',' and sValue != '(' and sValue != ';':
        lObjects[iObject] = token.identifier(sValue)
        return True
    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ',':
        lObjects[iObject] = token.comma()
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = token.colon()
        dVars['bInterfaceSignalDeclarationColonFound'] = True
        return True
    return False


def classify_mode_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() in lModes:
        lObjects[iObject] = token.mode_keyword(sValue)
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item and sValue.lower() != 'bus' and sValue.lower() not in lModes and sValue != ';':
            lObjects[iObject] = token.subtype_indication(sValue)
            return True
    return False


def classify_bus_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'bus':
        lObjects[iObject] = token.bus_keyword(sValue)
        return True
    return False


def classify_assignment_operator(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':=':
        lObjects[iObject] = token.assignment(':=')
        dVars['bInterfaceSignalDeclarationAssignmentOperatorFound'] = True
        return True
    return False


def classify_static_expression(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item and sValue.lower() != ':=':
        lObjects[iObject] = token.static_expression(sValue)
        return True
    return False


def clear_flags(dVars):
    dVars['bInterfaceSignalDeclarationAssignmentOperatorFound'] = False
    dVars['bInterfaceSignalDeclarationColonFound'] = False

