
from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import port_clause


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    entity_header ::=
        [ formal_generic_clause ]
        [ formal_port_clause ]
    '''
    if generic_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if port_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    generic_clause.clear_flags(dVars)
    port_clause.clear_flags(dVars)

