
from vsg.vhdlFile.classify import association_element

from vsg.token import association_list as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    association_list ::=
        association_element { , association_element }
    '''
    if classify_comma(oObject, iObject, lObjects, dVars):
        return True

    if association_element.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ',':
        lObjects[iObject] = token.comma()
        return True
    return False


def clear_flags(dVars):
    return True
