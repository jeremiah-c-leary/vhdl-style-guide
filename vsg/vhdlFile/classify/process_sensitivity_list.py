
from vsg.token import process_sensitivity_list as token

from vsg.vhdlFile.classify import sensitivity_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    process_sensitivity_list ::=
        all | sensitivity_list
    '''

    if classify_all_keyword(oObject, iObject, lObjects, dVars):
        return True

    if sensitivity_list.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_all_keyword(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue.lower() == 'all':
        lObjects[iObject] = token.all_keyword(sValue)
        return True
    return False

def clear_flags(dVars):
    sensitivity_list.clear(flags)
