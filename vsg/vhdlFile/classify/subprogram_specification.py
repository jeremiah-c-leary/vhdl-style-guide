
from vsg.vhdlFile.classify import procedure_specification
from vsg.vhdlFile.classify import function_specification

from vsg.token import subprogram_declaration as token


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    subprogram_specification ::=
        procedure_specification | function_specification
    '''
    if procedure_specification.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if function_specification.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False


def clear_flags(dVars):
    procedure_specification.clear_flags(dVars)    
    function_specification.clear_flags(dVars)    
