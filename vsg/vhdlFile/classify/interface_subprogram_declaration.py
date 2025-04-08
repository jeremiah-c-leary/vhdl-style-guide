# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_subprogram_declaration as token
from vsg.vhdlFile.classify import (
    interface_subprogram_default,
    interface_subprogram_specification,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_subprogram_declaration ::=
        interface_subprogram_specification [ is interface_subprogram_default ]
    """

    if interface_subprogram_specification.detect(oDataStructure):
        return oDataStructure.is_next_token("is")
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("is", token.is_keyword)

    interface_subprogram_default.classify(oDataStructure)
