
from vsg import parser
from vsg.token import file_type_definition as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    file_type_definition ::=
        file of type_mark
    ''' 

    if not dVars['type_declaration']['file_type_definition']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if classify_of_keyword(oObject, iObject, lObjects, dVars):
            return True 

        if classify_type_mark(oObject, iObject, lObjects, dVars):
            return True 

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'file':
        lObjects[iObject] = token.keyword(sValue)
        dVars['type_declaration']['file_type_definition']['keyword'] = True 
        return True
    return False


def classify_of_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'of':
        lObjects[iObject] = token.of_keyword(sValue)
        return True
    return False


def classify_type_mark(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = token.type_mark(oObject.get_value())
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['type_declaration']['file_type_definition']['keyword'] = False
