
from vsg import parser
from vsg.token import unbounded_array_definition as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    unbounded_array_definition ::=
        array ( index_subtype_definition { , index_subtype_definition } )
        of element_subtype_indication

    LIMITIATION:  index_subtype_definition and element_subtype_indication are not parsed.
    ''' 

    if not dVars['type_declaration']['array']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['type_declaration']['unbounded_array_declaration']['open_parenthesis']:

            if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                return True 

        else:


            if not dVars['type_declaration']['unbounded_array_declaration']['close_parenthesis']:

                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    return True 

                if classify_comma(oObject, iObject, lObjects, dVars):
                    return True 

                if classify_index_subtype_definition(oObject, iObject, lObjects, dVars):
                    return True 

            else:

                if classify_of_keyword(oObject, iObject, lObjects, dVars):
                    return True 

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


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['type_declaration']['unbounded_array_declaration']['open_parenthesis'] = True 
        return True
    return False


def classify_of_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'of':
        lObjects[iObject] = token.of_keyword(sValue)
        return True
    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ',':
        lObjects[iObject] = token.comma()
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == ')':
        lObjects[iObject] = token.close_parenthesis()
        dVars['type_declaration']['unbounded_array_declaration']['close_parenthesis'] = True 
        return True
    return False


def classify_index_subtype_definition(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.index_subtype_definition(oObject.get_value())
        return True
    return False


def classify_subtype_indication(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.subtype_indication(oObject.get_value())
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['array']['keyword'] = False
    dVars['type_declaration']['unbounded_array_declaration']['open_parenthesis'] = False
    dVars['type_declaration']['unbounded_array_declaration']['close_parenthesis'] = False
