# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    access_type_definition,
    composite_type_definition,
    file_type_definition,
    protected_type_definition,
    scalar_type_definition,
)


def detect(iToken, lObjects):
    """
    type_definition ::=
        scalar_type_definition
      | composite_type_definition
      | access_type_definition
      | file_type_definition
      | protected_type_definition
    """

    iReturn = scalar_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = access_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = composite_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = file_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    iReturn = protected_type_definition.detect(iToken, lObjects)
    if iReturn != iToken:
        return iReturn

    return iToken
