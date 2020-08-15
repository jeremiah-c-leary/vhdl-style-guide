
from vsg.token import sensitivity_list as token

from vsg.vhdlFile.classify import name


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    '''
    if classify_comma(oObject, iObject, lObjects, dVars):
        return True

    if name.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_comma(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ',':
        lObjects[iObject] = token.comma()
        return True
    return False


def clear_flags(dVars):
    name.clear_flags(dVars)
