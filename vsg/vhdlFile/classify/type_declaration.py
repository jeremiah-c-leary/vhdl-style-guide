
from vsg import parser
from vsg.token import type_declaration as token

from vsg.vhdlFile.classify import type_definition


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    full_type_declaration ::=
        type identifier is type_definition ;
    ''' 

    if not dVars['type_declaration']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['type_declaration']['isKeyword']:

            if classify_is_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True 

            if classify_identifier(oObject, iObject, lObjects, dVars):
                return True 

        else:

            if type_definition.tokenize(oObject, iObject, lObjects, dVars):
                return True 

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                type_definition.clear_flags(dVars)
                return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'type':
        lObjects[iObject] = token.keyword(sValue)
        dVars['type_declaration']['keyword'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(sValue)
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['type_declaration']['isKeyword'] = True
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['keyword'] = False
    dVars['type_declaration']['isKeyword'] = False
