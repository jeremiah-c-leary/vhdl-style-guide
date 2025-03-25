# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    alias_declaration,
    attribute_declaration,
    attribute_specification,
    component_declaration,
    constant_declaration,
    file_declaration,
    package_body,
    package_declaration,
    package_instantiation_declaration,
    subprogram_body,
    subprogram_declaration,
    subprogram_instantiation_declaration,
    subtype_declaration,
    type_declaration,
    use_clause,
    variable_declaration,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    package_body_declarative_item ::=
        subprogram_declaration
      | subprogram_body
      | subprogram_instantiation_declaration
      | package_declaration
      | package_body
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | variable_declaration
      | file_declaration
      | alias_declaration
      | attribute_declaration
      | attribute_specification
      | use_clause
      | group_template_declaration
      | group_declaration
    """

    if subprogram_declaration.detect(oDataStructure):
        subprogram_body.detect(oDataStructure)
        return True

    if subprogram_instantiation_declaration.detect(oDataStructure):
        return True

    if package_declaration.detect(oDataStructure):
        return True

    if package_body.detect(oDataStructure):
        return True

    if package_instantiation_declaration.detect(oDataStructure):
        return True

    if type_declaration.detect(oDataStructure):
        return True

    if subtype_declaration.detect(oDataStructure):
        return True

    if constant_declaration.detect(oDataStructure):
        return True

    if variable_declaration.detect(oDataStructure):
        return True

    if file_declaration.detect(oDataStructure):
        return True

    if alias_declaration.detect(oDataStructure):
        return True

    if component_declaration.detect(oDataStructure):
        return True

    if attribute_declaration.detect(oDataStructure):
        return True

    if attribute_specification.detect(oDataStructure):
        return True

    return use_clause.detect(oDataStructure)
