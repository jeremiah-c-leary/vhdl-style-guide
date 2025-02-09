# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import array_type_definition, record_type_definition


def detect(oDataStructure):
    """
    composite_type_definition ::=
        array_type_definition
      | record_type_definition
    """

    if array_type_definition.detect(oDataStructure):
        return True

    return record_type_definition.detect(oDataStructure)
