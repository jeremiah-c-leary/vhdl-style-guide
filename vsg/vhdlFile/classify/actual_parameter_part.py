
from vsg.vhdlFile.classify import association_list


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    actual_parameter_part ::= *parameter*_association_list
    '''

    if association_list.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    association_list.clear_flags(dVars)
