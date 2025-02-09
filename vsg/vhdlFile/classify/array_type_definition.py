# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    constrained_array_definition,
    unbounded_array_definition,
)


def detect(oDataStructure):
    """
    array_type_definition ::=
        unbounded_array_definition
      | constrained_array_definition
    """

    if unbounded_array_definition.detect(oDataStructure):
        return True

    return constrained_array_definition.detect(oDataStructure)
