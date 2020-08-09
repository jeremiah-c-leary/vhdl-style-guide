
from vsg import parser
from vsg.token import access_type_definition as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    access_type_definition ::=

        access subtype_indication

    LIMITIATION:  subtype_indication is not parsed.
    ''' 

    if not dVars['type_declaration']['access_definition']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if classify_subtype_indication(oObject, iObject, lObjects, dVars):
            return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'access':
        lObjects[iObject] = token.keyword(sValue)
        dVars['type_declaration']['access_definition']['keyword'] = True 
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item and oObject.get_value() != ';':
        lObjects[iObject] = token.subtype_indication(oObject.get_value())
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['access_definition']['keyword'] = False
