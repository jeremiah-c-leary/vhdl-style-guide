
from vsg.token import port_clause as token


def beginning(dVars, lObjects):
    '''
    Classifies the beginning portion of port clauses:

        port ( 
    '''
    for iObject, oObject in enumerate(lObjects):
        if not dVars['bPortClauseKeywordFound']:
            classify_keyword(oObject, iObject, lObjects, dVars)
        else:
            if not dVars['bPortClauseOpenParenthesisFound']:
                if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                    break


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'port':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bPortClauseKeywordFound'] = True


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['bPortClauseOpenParenthesisFound'] = True
        return True
    return False


def ending(dVars, lObjects):
    '''
    Classifies the ending portion of port clauses:

        ) ;
    '''
    for iObject, oObject in enumerate(lObjects):
        classify_close_parenthesis(oObject, iObject, lObjects, dVars)
        if classify_semicolon(oObject, iObject, lObjects, dVars):
            break


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        lObjects[iObject] = token.close_parenthesis()


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        dVars['bPortClauseKeywordFound'] = False
        dVars['bPortClauseOpenParenthesisFound'] = False
        return True
    return False
