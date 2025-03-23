# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import procedure_specification as token
from vsg.vhdlFile.classify import formal_parameter_list, subprogram_header


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    procedure_specification ::=
        procedure designator
            subprogram_header
            [ [ parameter ] ( formal_parameter_list ) ]
    """

    if oDataStructure.is_next_token("procedure"):
        if not oDataStructure.does_string_exist_in_next_n_tokens("new", 4):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.procedure_keyword)
    oDataStructure.replace_next_token_with(token.designator)

    subprogram_header.detect(oDataStructure)

    oDataStructure.replace_next_token_with_if("parameter", token.parameter_keyword)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(token.open_parenthesis)
        formal_parameter_list.classify(oDataStructure)
        oDataStructure.replace_next_token_required(")", token.close_parenthesis)
