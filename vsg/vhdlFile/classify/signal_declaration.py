import re

from vsg import parser
from vsg.token import signal_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    signal identifier { , identifier } : subtype_indication [ signal kind ] [ := expression ] ;
  
    '''
    if not dVars['bSignalKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['bSignalColonFound']:

            if classify_colon(oObject, iObject, lObjects, dVars):
                return True

            if classify_comma(oObject, iObject, lObjects):
                return True

            if classify_identifier(oObject, iObject, lObjects):
                return True

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True

            if not dVars['bSignalAssignmentOperatorFound']:

                if classify_assignment_operator(oObject, iObject, lObjects, dVars):
                    return True

                if classify_signal_kind(oObject, iObject, lObjects):
                    return True

                if classify_subtype_indication(oObject, iObject, lObjects):
                    return True

            else:

                if classify_assignment_expression(oObject, iObject, lObjects):
                    return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'signal':
        lObjects[iObject] = signal_declaration.keyword(sValue)
        dVars['bSignalKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = signal_declaration.identifier(oObject.get_value())
        return True
    return False


def classify_comma(oObject, iObject, lObjects):
    if oObject.get_value() == ',':
        lObjects[iObject] = signal_declaration.comma()
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = signal_declaration.colon()
        dVars['bSignalColonFound'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = signal_declaration.subtype_indication(oObject.get_value())
        return True
    return False


def classify_signal_kind(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        sValue = oObject.get_value()
        if sValue.lower() == 'bus' or sValue.lower() == 'register':
            lObjects[iObject] = signal_declaration.signal_kind(oObject.get_value())
            return True
    return False


def classify_assignment_operator(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':=':
        lObjects[iObject] = signal_declaration.assignment_operator()
        dVars['bSignalAssignmentOperatorFound'] = True
        return True
    return False


def classify_assignment_expression(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = signal_declaration.assignment_expression(oObject.get_value)
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = signal_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
        dVars['bSignalKeywordFound'] = False
        dVars['bSignalColonFound'] = False
        dVars['bSignalAssignmentOperatorFound'] = False
