
from vsg.token import generic_clause as token

from vsg.vhdlFile.classify import interface_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    Classifies generic clauses:

        generic ( generic_list ) ;
    '''
    if not dVars['bGenericClauseKeywordFound']:
        classify_keyword(oObject, iObject, lObjects, dVars)
    else:
        if not dVars['bGenericClauseOpenParenthesisFound']:
            classify_open_parenthesis(oObject, iObject, lObjects, dVars)
        else:
            if not dVars['bGenericClauseCloseParenthesisFound']:
                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    interface_list.clear_flags(dVars)
                    return True
                interface_list.interface_list(oObject, iObject, lObjects, dVars)
            else:
                classify_semicolon(oObject, iObject, lObjects, dVars)



def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'generic':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bGenericClauseKeywordFound'] = True


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['bGenericClauseOpenParenthesisFound'] = True


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        lObjects[iObject] = token.close_parenthesis()
        dVars['bGenericClauseCloseParenthesisFound'] = True
        return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)

def clear_flags(dVars):
    interface_list.clear_flags(dVars)
    dVars['bGenericClauseKeywordFound'] = False
    dVars['bGenericClauseOpenParenthesisFound'] = False
    dVars['bGenericClauseCloseParenthesisFound'] = False

