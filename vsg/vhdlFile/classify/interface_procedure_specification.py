# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_procedure_specification as token
from vsg.vhdlFile.classify import formal_parameter_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    interface_procedure_specification ::=
        procedure designator
            [ [ parameter ] ( formal_parameter_list ) ]
    """
    return oDataStructure.is_next_token("procedure")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.procedure_keyword)
    oDataStructure.replace_next_token_with(token.designator)
    oDataStructure.replace_next_token_with_if("parameter", token.parameter_keyword)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(token.open_parenthesis)
        formal_parameter_list.classify(oDataStructure)
        oDataStructure.replace_next_token_required(")", token.close_parenthesis)
