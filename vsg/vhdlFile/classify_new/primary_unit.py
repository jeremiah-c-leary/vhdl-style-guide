
from vsg.vhdlFile.classify_new import context_declaration
from vsg.vhdlFile.classify_new import package_declaration


def detect(iCurrent, lObjects):
    '''
    primary_unit ::=
        entity_declaration
      | configuration_declaration
      | package_declaration
      | package_instantiation_declaration
      | context_declaration
      | PSL_Verification_Unit
    '''
    iReturned = context_declaration.detect(iCurrent, lObjects)
    if iReturned != iCurrent:
        return iReturned

    iReturned = package_declaration.detect(iCurrent, lObjects)
    if iReturned != iCurrent:
        return iReturned

    return iCurrent
