# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import function_specification, procedure_specification


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_specification ::=
        procedure_specification
      | function_specification
    """

    if procedure_specification.detect(oDataStructure):
        return True

    return function_specification.detect(oDataStructure)
