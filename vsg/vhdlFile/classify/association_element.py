
#from vsg.vhdlFile.classify import formal_part
#from vsg.vhdlFile.classify import actual_part

from vsg.token import association_element as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    association_element ::=
        [ formal_part => ] actual_part
    '''
    if classify_assignment(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_assignment(oObject, iObject, lObjects, dVars):
    sValue = oObject.get_value()
    if sValue == '=>':
        lObjects[iObject] = token.assignment(sValue)
        return True
    return False


def clear_flags(dVars):
    return True
