
from vsg.vhdlFile.classify import generic_clause


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    package_header ::=
        [ generic_clause
        { generic_map_aspect ; ] ]
    '''
    if generic_clause.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
