
from vsg import parser
from vsg.token import attribute_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    attribute_declaration ::=
        attribute identifier : type_mark ;
    '''

    if not dVars['bAttributeKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['bAttributeColonFound']:

            if classify_colon(oObject, iObject, lObjects, dVars):
                return True 

            if classify_identifier(oObject, iObject, lObjects):
                return True 

        else:

            if classify_semicolon(oObject, iObject, lObjects, dVars):
                return True 

            if classify_type_mark(oObject, iObject, lObjects):
                return True 


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'attribute':
        lObjects[iObject] = attribute_declaration.keyword(sValue)
        dVars['bAttributeKeywordFound'] = True 
        return True
    return False


def classify_identifier(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = attribute_declaration.identifier(oObject.get_value())
        return True
    return False


def classify_colon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ':':
        lObjects[iObject] = attribute_declaration.colon()
        dVars['bAttributeColonFound'] = True
        return True
    return False


def classify_type_mark(oObject, iObject, lObjects):
    if type(oObject) == parser.item:
        lObjects[iObject] = attribute_declaration.type_mark(oObject.get_value())
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = attribute_declaration.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['bAttributeKeywordFound'] = False
    dVars['bAttributeColonFound'] = False

