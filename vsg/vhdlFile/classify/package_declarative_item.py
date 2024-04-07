# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    alias_declaration,
    attribute_declaration,
    attribute_specification,
    component_declaration,
    constant_declaration,
    file_declaration,
    package_declaration,
    package_instantiation_declaration,
    signal_declaration,
    subprogram_declaration,
    subprogram_instantiation_declaration,
    subtype_declaration,
    type_declaration,
    use_clause,
    variable_declaration,
)


def detect(iToken, lObjects):
    """
    package_declarative_item ::=
        subprogram_declaration
      | subprogram_instantiation_declaration
      | package_declaration
      | package_instantiation_declaration
      | type_declaration
      | subtype_declaration
      | constant_declaration
      | signal_declaration
      | variable_declaration
      | file_declaration
      | alias_declaration
      | component_declaration
      | attribute_declaration
      | attribute_specification
      | disconnection_specification
      | use_clause
      | group_template_declaration
      | group_declaration
      | PSL_Property_Declaration
      | PSL_Sequence_Declaration
    """

    iReturn = subprogram_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = subprogram_instantiation_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = package_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = package_instantiation_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = type_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = subtype_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = constant_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = signal_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = variable_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = file_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = alias_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = component_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = attribute_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = attribute_specification.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = use_clause.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
