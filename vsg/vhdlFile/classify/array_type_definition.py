
from vsg.vhdlFile.classify import constrained_array_definition
from vsg.vhdlFile.classify import unbounded_array_definition


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    array_type_definition ::=
        unbounded_array_definition
      | constrained_array_definition

    ''' 
    if constrained_array_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True 

    if unbounded_array_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True 

    return False


def clear_flags(dVars):
    constrained_array_definition.clear_flags(dVars)
    unbounded_array_definition.clear_flags(dVars)

