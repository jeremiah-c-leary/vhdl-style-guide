
from vsg.vhdlFile.classify import configuration_declaration
from vsg.vhdlFile.classify import context_declaration
from vsg.vhdlFile.classify import entity_declaration
from vsg.vhdlFile.classify import package_declaration
from vsg.vhdlFile.classify import package_instantiation_declaration


def detect(iToken, lObjects):
    '''
    primary_unit ::=
        entity_declaration
      | configuration_declaration
      | package_declaration
      | package_instantiation_declaration
      | context_declaration
      | PSL_Verification_Unit
    '''

    iReturned = context_declaration.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    iReturned = entity_declaration.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    iReturned = package_declaration.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    iReturned = package_instantiation_declaration.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    iReturned = configuration_declaration.detect(iToken, lObjects)
    if iReturned != iToken:
        return iReturned

    return iToken
