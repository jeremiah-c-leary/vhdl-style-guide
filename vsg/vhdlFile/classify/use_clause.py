
from vsg import parser
from vsg.token import use_clause


def tokenize(oObject, iObject, lObjects, dVars):

    '''
    use_clause ::=
        use selected_name { , selected_name } ;
    '''
    
    if not dVars['bUseClauseKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if classify_semicolon(oObject, iObject, lObjects, dVars):
            return True 

        if classify_comma(oObject, iObject, lObjects, dVars):
            return True 

        if classify_selected_name(oObject, iObject, lObjects, dVars):
            return True 


    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'use':
        lObjects[iObject] = use_clause.keyword(sValue)
        dVars['bUseClauseKeywordFound'] = True
        return True
    return False


def classify_selected_name(oObject, iObject, lObjects, dVars):
    if type(oObject) == parser.item:
        lObjects[iObject] = use_clause.selected_name(oObject.get_value())
        return True
    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ',':
        lObjects[iObject] = use_clause.comma()
        clear_flags(dVars)
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = use_clause.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    dVars['bUseClauseKeywordFound'] = False
