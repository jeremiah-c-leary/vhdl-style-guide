
from vsg.vhdlFile.classify import context_clause
from vsg.vhdlFile.classify import library_unit


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    design_unit ::= context_clause library_unit
    '''
    if context_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if library_unit.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
