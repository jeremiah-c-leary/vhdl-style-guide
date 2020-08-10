
from vsg.vhdlFile.classify import subprogram_specification

from vsg.token import subprogram_declaration as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    subprogram_declaration ::=
        subprogram_specification ;
    '''
    if subprogram_specification.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if dVars['procedure_specification']['close_parenthesis'] or dVars['function_specification']['return']:
        if classify_semicolon(oObject, iObject, lObjects, dVars):
            return True

    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    subprogram_specification.clear_flags(dVars)
