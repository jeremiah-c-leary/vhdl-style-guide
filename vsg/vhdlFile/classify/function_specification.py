# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import function_specification as token
from vsg.vhdlFile.classify import formal_parameter_list, subprogram_header, type_mark


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    function_specification ::=
        [ pure | impure ] function designator
            subprogram_header
            [ [ parameter ] ( formal_parameter_list ) ] return type_mark
    """

    if oDataStructure.is_next_token_one_of(["pure", "impure", "function"]):
        if not oDataStructure.does_string_exist_in_next_n_tokens("new", 4):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("pure", token.pure_keyword)
    oDataStructure.replace_next_token_with_if("impure", token.impure_keyword)
    oDataStructure.replace_next_token_required("function", token.function_keyword)
    oDataStructure.replace_next_token_with(token.designator)

    subprogram_header.detect(oDataStructure)

    oDataStructure.replace_next_token_with_if("parameter", token.parameter_keyword)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(token.open_parenthesis)
        formal_parameter_list.classify(oDataStructure)
        oDataStructure.replace_next_token_required(")", token.close_parenthesis)

    oDataStructure.replace_next_token_required("return", token.return_keyword)
    type_mark.classify(oDataStructure)
