
from vsg import parser
from vsg.token import subtype_declaration as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    subtype_declaration ::=
        subtype identifier is subtype_indication ;

    LIMITIATION:  subtype_indication is not parsed.
    ''' 

    if not dVars['subtype_declaration']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['subtype_declaration']['isKeyword']:

            if classify_is_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_identifier(oObject, iObject, lObjects, dVars):
                return True 

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True 

            if classify_subtype_indication(oObject, iObject, lObjects, dVars):
                return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'subtype':
        lObjects[iObject] = token.keyword(sValue)
        dVars['subtype_declaration']['keyword'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(oObject.get_value())
        return True
    return False


def classify_is_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'is':
        lObjects[iObject] = token.is_keyword(sValue)
        dVars['subtype_declaration']['isKeyword'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.subtype_indication(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['subtype_declaration']['keyword'] = False
    dVars['subtype_declaration']['isKeyword'] = False
