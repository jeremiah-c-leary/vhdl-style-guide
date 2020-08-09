
from vsg import parser
from vsg.token import constrained_array_definition as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    constrained_array_definition ::=
        array index_constraint of element_subtype_indication

    LIMITIATION:  index_subtype_definition and element_subtype_indication are not parsed.
    ''' 

    if not dVars['type_declaration']['array']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['type_declaration']['constrained_array_declaration']['of_keyword']:

            if classify_of_keyword(oObject, iObject, lObjects, dVars):
                return True 

            if classify_index_constraint(oObject, iObject, lObjects, dVars):
                return True 

        else:

            if classify_subtype_indication(oObject, iObject, lObjects, dVars):
                return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'array':
#        lObjects[iObject] = token.keyword(sValue)
        dVars['type_declaration']['array']['keyword'] = True 
        return True
    return False


def classify_index_constraint(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.index_constraint(oObject.get_value())
        return True
    return False


def classify_of_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'of':
        lObjects[iObject] = token.of_keyword(sValue)
        dVars['type_declaration']['constrained_array_declaration']['of_keyword'] = True
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item and oObject.get_value() != ';':
        lObjects[iObject] = token.subtype_indication(oObject.get_value())
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['array']['keyword'] = False
    dVars['type_declaration']['constrained_array_declaration']['of_keyword'] = False
