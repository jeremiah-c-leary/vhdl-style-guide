
from vsg.vhdlFile.classify import access_type_definition
from vsg.vhdlFile.classify import composite_type_definition
from vsg.vhdlFile.classify import file_type_definition
from vsg.vhdlFile.classify import protected_type_definition
from vsg.vhdlFile.classify import scalar_type_definition


def tokenize(oObject, iObject, lObjects, dVars):
    '''
        type_definition ::=
            scalar_type_definition
          | composite_type_definition
          | access_type_definition
          | file_type_definition
          | protected_type_definition
    '''
    if not composite_type_found(dVars):
        if scalar_type_definition.tokenize(oObject, iObject, lObjects, dVars):
            return True

    if composite_type_definition.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if not composite_type_found(dVars):
        if access_type_definition.tokenize(oObject, iObject, lObjects, dVars):
            return True

    if not composite_type_found(dVars):
        if file_type_definition.tokenize(oObject, iObject, lObjects, dVars):
            return True

    if not composite_type_found(dVars):
        if protected_type_definition.tokenize(oObject, iObject, lObjects, dVars):
            return True

    return False


def clear_flags(dVars):
    scalar_type_definition.clear_flags(dVars)
    composite_type_definition.clear_flags(dVars)
    access_type_definition.clear_flags(dVars)
    file_type_definition.clear_flags(dVars)
    protected_type_definition.clear_flags(dVars)


def composite_type_found(dVars):
    if dVars['type_declaration']['array']['keyword'] or dVars['type_declaration']['record_type_definition']['keyword']:
        return True
    return False
