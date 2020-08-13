
from vsg.token import interface_list as token
from vsg.vhdlFile.classify import interface_element


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    Classifies interface_lists

    interface_list ::= interface_element { ; interface_element }

    '''
    if classify_semicolon(oObject, iObject, lObjects, dVars):
        return True

    if interface_element.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
            

def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        clear_flags(dVars)
        return True
    return False


def clear_flags(dVars):
    interface_element.clear_flags(dVars)
