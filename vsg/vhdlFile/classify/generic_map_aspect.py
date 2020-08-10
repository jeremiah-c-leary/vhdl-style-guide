
from vsg.vhdlFile.classify import association_list

from vsg.token import generic_map_aspect as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    generic_map_aspect ::=
        generic map ( *generic*_association_list )
    '''
    if not dVars['generic_map_aspect']['keyword']:

        if classify_keyword(oObject, iObject, lObjects, dVars):
            return True

    else:

        if not dVars['generic_map_aspect']['open_parenthesis']:

            if classify_open_parenthesis(oObject, iObject, lObjects, dVars):
                return True

            if classify_map_keyword(oObject, iObject, lObjects, dVars):
                return True

        else:
  
            if not dVars['generic_map_aspect']['close_parenthesis']: 

                if classify_close_parenthesis(oObject, iObject, lObjects, dVars):
                    return True
        
                if association_list.tokenize(oObject, iObject, lObjects, dVars):
                    return True

    return False


def classify_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'generic':
        lObjects[iObject] = token.keyword(sValue)
        dVars['generic_map_aspect']['keyword'] = True
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
        dVars['generic_map_aspect']['open_parenthesis'] = True
        return True
    return False


def classify_close_parenthesis(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ')':
        lObjects[iObject] = token.close_parenthesis()
        dVars['generic_map_aspect']['close_parenthesis'] = True
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    association_list.clear_flags(dVars)
    dVars['generic_map_aspect']['keyword'] = False
    dVars['generic_map_aspect']['open_parenthesis'] = False
    dVars['generic_map_aspect']['close_parenthesis'] = False
