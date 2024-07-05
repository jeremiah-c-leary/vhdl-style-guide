# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    attribute_specification,
    subprogram_body,
    subprogram_declaration,
    subprogram_instantiation_declaration,
    use_clause,
)


def detect(iToken, lObjects):
    """
    protected_type_declarative_item ::=
        subprogram_declaration
      | subprogram_instantiation_declaration
      | attribute_specification
      | use_clause
    """

    iReturn = subprogram_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        iReturn = subprogram_body.detect(iReturn, lObjects)
        return iReturn

    iReturn = subprogram_instantiation_declaration.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = attribute_specification.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = use_clause.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
