# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    attribute_specification,
    subprogram_body,
    subprogram_declaration,
    subprogram_instantiation_declaration,
    use_clause,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    protected_type_declarative_item ::=
        subprogram_declaration
      | subprogram_instantiation_declaration
      | attribute_specification
      | use_clause
    """

    if subprogram_declaration.detect(oDataStructure):
        subprogram_body.detect(oDataStructure)
        return True

    if subprogram_instantiation_declaration.detect(oDataStructure):
        return True

    if attribute_specification.detect(oDataStructure):
        return True

    if use_clause.detect(oDataStructure):
        return True

    return False
