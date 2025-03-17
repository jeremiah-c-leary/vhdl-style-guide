# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import (
    external_constant_name,
    external_signal_name,
    external_variable_name,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    external_name ::=
        external_constant_name
      | external_signal_name
      | external_variable_name
    """

    if external_constant_name.detect(oDataStructure):
        return True

    if external_signal_name.detect(oDataStructure):
        return True

    return external_variable_name.detect(oDataStructure)
