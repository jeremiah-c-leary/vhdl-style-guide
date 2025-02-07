# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import simple_configuration_specification


def detect(oDataStructure):
    """
    configuration_specification ::=
        simple_configuration_specification
      | compound_configuration_specification
    """
    return simple_configuration_specification.detect(oDataStructure)
