
from vsg import parser

from vsg.vhdlFile.classify import range_constraint


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    integer_type_definition ::=
        range_constraint
    ''' 

    if range_constraint.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):

    range_constraint.clear_flags(dVars)
