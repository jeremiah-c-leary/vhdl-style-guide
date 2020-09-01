
from vsg.vhdlFile.classify_new import context_clause
#from vsg.vhdlFile.classify_new import library_unit


def detect(iCurrent, lObjects):
    '''
    design_unit ::=
        context_clause library_unit
    '''
    iReturned = context_clause.detect(iCurrent, lObjects)

#    if library_unit.tokenize(oObject, iObject, lObjects, dVars):
#        return True
#
#    return False
