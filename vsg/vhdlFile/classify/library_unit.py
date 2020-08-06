
from vsg.vhdlFile.classify import primary_unit
from vsg.vhdlFile.classify import secondary_unit


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    library_unit ::=
        primary_unit
      | secondary_unit
    '''

    if primary_unit.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if secondary_unit.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
