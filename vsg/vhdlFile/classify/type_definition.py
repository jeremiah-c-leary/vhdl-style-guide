# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    access_type_definition,
    composite_type_definition,
    file_type_definition,
    protected_type_definition,
    scalar_type_definition,
)


def detect(oDataStructure):
    """
    type_definition ::=
        scalar_type_definition
      | composite_type_definition
      | access_type_definition
      | file_type_definition
      | protected_type_definition
    """

    if scalar_type_definition.detect(oDataStructure):
        return True

    if access_type_definition.detect(oDataStructure):
        return True

    if composite_type_definition.detect(oDataStructure):
        return True

    if file_type_definition.detect(oDataStructure):
        return True

    return protected_type_definition.detect(oDataStructure)
