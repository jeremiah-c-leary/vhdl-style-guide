
from vsg.token import block_header as token

from vsg.vhdlFile.classify import generic_clause
from vsg.vhdlFile.classify import generic_map_aspect

from vsg.vhdlFile.classify import port_clause
from vsg.vhdlFile.classify import port_map_aspect


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    block_header ::=
        [ generic_clause
        [ generic_map_aspect ; ] ]
        [ port_clause
        [ port_map_aspect ; ] ]
    '''
    if generic_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if generic_map_aspect.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if port_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if port_map_aspect.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if classify_semicolon(oObject, iObject, lObjects, dVars):
        return True

    return False


def classify_semicolon(oObject, iObject, lObjects, dVars):
    if oObject.get_value() == ';':
        lObjects[iObject] = token.semicolon()
        return True
    return False


def clear_flags(dVars):
    generic_clause.clear_flags(dVars)
    generic_map_aspect.clear_flags(dVars)
    port_clause.clear_flags(dVars)
    port_map_aspect.clear_flags(dVars)
