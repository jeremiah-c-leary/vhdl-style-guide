
from vsg import parser
from vsg.token import element_declaration as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    element_declaration ::=
        identifier_list : element_subtype_definition ;

    LIMITIATION:  element_subtype_definition is not parsed.
    ''' 

    if not dVars['type_declaration']['record_type_definition']['element_declaration']['colon']:

        if classify_colon(oObject, iObject, lObjects, dVars):
            return True 

        if classify_comma(oObject, iObject, lObjects, dVars):
            return True 

        if classify_identifier(oObject, iObject, lObjects, dVars):
            return True

    else:

        if classify_semicolon(oObject, iObject, lObjects, dVars):
            return True 

        if classify_subtype_definition(oObject, iObject, lObjects, dVars):
            return True 

    return False


def classify_identifier(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.identifier(oObject.get_value())
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
        dVars['type_declaration']['record_type_definition']['element_declaration']['colon'] = True
        return True
    return False


def classify_subtype_definition(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.element_subtype_definition(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['record_type_definition']['element_declaration']['colon'] = False
