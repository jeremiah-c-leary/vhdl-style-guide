
from vsg.vhdlFile.classify import entity_declaration
from vsg.vhdlFile.classify import package_declaration


def tokenize(oObject, iObject, lObjects, dVars):
    '''
    primary_unit ::=
        entity_declaration
      | configuration_declaration
      | package_declaration
      | package_instantiation_declaration
      | context_declaration
      | PSL_Verification_Unit
    ''' 

    if entity_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    if package_declaration.tokenize(oObject, iObject, lObjects, dVars):
        return True

    return False
