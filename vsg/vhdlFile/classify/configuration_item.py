# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import block_configuration, component_configuration


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    return classify(iToken, lObjects)


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    configuration_item ::=
        block_configuration
      | component_configuration
    """

    iCurrent = component_configuration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = block_configuration.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
