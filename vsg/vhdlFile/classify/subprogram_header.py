
from vsg.vhdlFile.classify import generic_list
from vsg.vhdlFile.classify import generic_map_aspect

from vsg.token import subprogram_header as token

iOpenParenthesis = 0
iCloseParenthesis = 0


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    subprogram_header ::=
        [ generic ( generic_list )
        [ generic_map_aspect ] ]
    '''
    if not dVars['subprogram_header']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['subprogram_header']['open_parenthesis']:

            if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                return True

        else:
  
            update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis)

            if not dVars['subprogram_header']['close_parenthesis']: 

                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    return True
        
                if generic_list.tokenize(oObject, iObject, lObjects, dVars):
                    return True

            else:

                if generic_map_aspect.tokenize(oObject, iObject, lObjects, dVars):
                    return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'generic':
        lObjects[iObject] = token.keyword(sValue)
        dVars['subprogram_header']['keyword'] = True
        return True
    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        iOpenParenthesis = 1
        iCloseParenthesis = 0
        dVars['subprogram_header']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        if iOpenParenthesis == iCloseParenthesis:
            lObjects[iObject] = token.close_parenthesis()
            dVars['subprogram_header']['close_parenthesis'] = True
            return True
    return False


def clear_flags(dVars):
    generic_list.clear_flags(dVars)
    generic_map_aspect.clear_flags(dVars)
    dVars['subprogram_header']['keyword'] = False
    dVars['subprogram_header']['open_parenthesis'] = False
    dVars['subprogram_header']['close_parenthesis'] = False


def update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis):
    if oObject.get_value() == '(':
        iOpenParenthesis += 1
    if oObject.get_value() == ')':
        iCloseParenthesis += 1
