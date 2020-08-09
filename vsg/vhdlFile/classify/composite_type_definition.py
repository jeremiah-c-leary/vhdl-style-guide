
from vsg.vhdlFile.classify import array_type_definition
from vsg.vhdlFile.classify import record_type_definition


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    composite_type_definition ::= 
        array_type_definition
      | record_type_definition
    '''
    if not record_type_found(dVars):
        if array_type_definition.tokenize(oObject, iObject, lObjects, dVars):
            return True

    if not array_type_found(dVars):
        if record_type_definition.tokenize(oObject, iObject, lObjects, dVars):
            return True

    return False


def clear_flags(dVars):
    array_type_definition.clear_flags(dVars)
    record_type_definition.clear_flags(dVars)


def record_type_found(dVars):
    return dVars['type_declaration']['record_type_definition']['keyword']

def array_type_found(dVars):
    return dVars['type_declaration']['array']['keyword']
