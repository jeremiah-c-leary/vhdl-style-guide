# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    interface_function_specification,
    interface_procedure_specification,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(iToken, lObjects):
    """
    interface_subprogram_specification ::=
        interface_procedure_specification
      | interface_function_specification
    """

    iCurrent = interface_procedure_specification.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    iCurrent = interface_function_specification.detect(iToken, lObjects)
    if iCurrent != iToken:
        return iCurrent

    return iToken
