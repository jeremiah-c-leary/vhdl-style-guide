# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import simple_configuration_specification


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    configuration_specification ::=
        simple_configuration_specification
      | compound_configuration_specification
    """
    return simple_configuration_specification.detect(oDataStructure)
