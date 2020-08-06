
from vsg.vhdlFile.classify import design_unit


def tokenize(oObject, iObject, lObjects, dVars):

    '''
    design_file ::= design_unit { design_unit }
    '''
    if design_unit.tokenize(oObject, iObject, lObjects, dVars):
        return True 

    return False
