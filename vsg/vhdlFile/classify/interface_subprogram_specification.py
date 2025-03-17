# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import (
    interface_function_specification,
    interface_procedure_specification,
)
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_subprogram_specification ::=
        interface_procedure_specification
      | interface_function_specification
    """

    if interface_procedure_specification.detect(oDataStructure):
        interface_procedure_specification.classify(oDataStructure)
        return True 

    if interface_function_specification.detect(oDataStructure):
        interface_function_specification.classify(oDataStructure)
        return True 

    return False
