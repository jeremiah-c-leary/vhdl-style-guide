# -*- coding: utf-8 -*-

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
    signal_declaration,
    subprogram_body,
    subprogram_declaration,
    subprogram_instantiation_declaration,
    subtype_declaration,
    type_declaration,
    use_clause,
    variable_declaration,
)


def detect(iToken, lObjects):
    """
    entity_declarative_item ::=
        subprogram_declaration
      | subprogram_body
      | subprogram_instantiation_declaration
      | package_declaration
      | package_body
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | signal_declaration
      | *shared*_variable_declaration
      | file_declaration
      | alias_declaration
      | attribute_declaration
      | attribute_specification
      | disconnection_specification
      | use_clause
      | group_template_declaration
      | group_declaration
      | PSL_Property_Declaration
      | PSL_Sequence_Declaration
      | PSL_Clock_Declaration
    """

    iCurrent = subprogram_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        iCurrent = subprogram_body.detect(iCurrent, lObjects)
        return iCurrent

    iCurrent = subprogram_instantiation_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = package_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = package_body.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = package_instantiation_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = type_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = subtype_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = constant_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = signal_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = variable_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = file_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = alias_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = component_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = attribute_declaration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = attribute_specification.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = use_clause.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
