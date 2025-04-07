# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import block_configuration, component_configuration


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    configuration_item ::=
        block_configuration
      | component_configuration
    """

    if component_configuration.detect(oDataStructure):
        return True

    return block_configuration.detect(oDataStructure)
