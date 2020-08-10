
from vsg.token import port_clause as token

from vsg.vhdlFile.classify import interface_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    Classifies the beginning portion of port clauses:

        port ( port_list ) ;

    '''
    if not dVars['bPortClauseKeywordFound']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True 

    else:

        if not dVars['bPortClauseOpenParenthesisFound']:

            if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                return True 

        else:

            update_parenthesis_counts(oObject, dVars)

            if not dVars['bPortClauseCloseParenthesisFound']:

                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    interface_list.clear_flags(dVars)
                    return True

                if interface_list.interface_list(oObject, iObject, lObjects, dVars):
                    return True 

            else:

                if classify_semicolon(oObject, iObject, lObjects, dVars):
                    return True 



def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'port':
        lObjects[iObject] = token.keyword(sValue)
        dVars['bPortClauseKeywordFound'] = True
        return True
    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['bPortClauseOpenParenthesisFound'] = True
        dVars['iOpenParenthesisCount'] = 1
        dVars['iCloseParenthesisCount'] = 0
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        if dVars['iOpenParenthesisCount'] == dVars['iCloseParenthesisCount']:        
            dVars['bPortClauseCloseParenthesisFound'] = True
            lObjects[iObject] = token.close_parenthesis()
            return True
    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def update_parenthesis_counts(oObject, dVars):
    if oObject.get_value() == '(':
        dVars['iOpenParenthesisCount'] += 1
    if oObject.get_value() == ')':
        dVars['iCloseParenthesisCount'] += 1


def clear_flags(dVars):
    interface_list.clear_flags(dVars)
    dVars['bPortClauseKeywordFound'] = False
    dVars['bPortClauseOpenParenthesisFound'] = False
    dVars['bPortClauseCloseParenthesisFound'] = False

