
from vsg.vhdlFile.classify import association_list

from vsg.token import port_map_aspect as token

iOpenParenthesis = 0
iCloseParenthesis = 0


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    port_map_aspect ::=
        port map ( *port*_association_list )
    '''
    if not dVars['port_map_aspect']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['port_map_aspect']['open_parenthesis']:

            if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                return True

            if classify_map_keyword(oObject, iObject, lObjects, dVars):
                return True

        else:
  
            if not dVars['port_map_aspect']['close_parenthesis']: 

                update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis)

                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    return True
        
                if association_list.tokenize(oObject, iObject, lObjects, dVars):
                    return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'port':
        lObjects[iObject] = token.keyword(sValue)
        dVars['port_map_aspect']['keyword'] = True
        return True
    return False


def classify_map_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'map':
        lObjects[iObject] = token.map_keyword(sValue)
        return True
    return False


def classify_open_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == '(':
        lObjects[iObject] = token.open_parenthesis()
        dVars['port_map_aspect']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        if iOpenParenthesis == iCloseParenthesis:
            lObjects[iObject] = token.close_parenthesis()
            dVars['port_map_aspect']['close_parenthesis'] = True
            clear_flags(dVars)
            return True
    return False


def clear_flags(dVars):
    association_list.clear_flags(dVars)
    dVars['port_map_aspect']['keyword'] = False
    dVars['port_map_aspect']['open_parenthesis'] = False
    dVars['port_map_aspect']['close_parenthesis'] = False


def update_parenthesis_counts(oObject, iOpenParenthesis, iCloseParenthesis):
    if oObject.get_value() == '(':
        iOpenParenthesis += 1
    if oObject.get_value() == ')':
        iCloseParenthesis += 1
