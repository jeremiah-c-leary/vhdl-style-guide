# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    configuration_declaration,
    context_declaration,
    entity_declaration,
    package_declaration,
    package_instantiation_declaration,
    psl_verification_unit,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    primary_unit ::=
        entity_declaration
      | configuration_declaration
      | package_declaration
      | package_instantiation_declaration
      | context_declaration
      | PSL_Verification_Unit
    """

    if context_declaration.detect(oDataStructure):
        return True

    if entity_declaration.detect(oDataStructure):
        return True

    if package_declaration.detect(oDataStructure):
        return True

    if package_instantiation_declaration.detect(oDataStructure):
        return True

    if configuration_declaration.detect(oDataStructure):
        return True

    return psl_verification_unit.detect(oDataStructure)
