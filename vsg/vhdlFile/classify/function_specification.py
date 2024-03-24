# -*- coding: utf-8 -*-

from vsg.token import function_specification as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import formal_parameter_list, subprogram_header, type_mark


def detect(iToken, lObjects):
    """
    function_specification ::=
        [ pure | impure ] function designator
            subprogram_header
            [ [ parameter ] ( formal_parameter_list ) ] return type_mark
    """

    if utils.is_next_token_one_of(["pure", "impure", "function"], iToken, lObjects):
        if not utils.find_in_next_n_tokens("new", 4, iToken, lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_if("pure", token.pure_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("impure", token.impure_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_required("function", token.function_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.designator, iCurrent, lObjects)

    iCurrent = subprogram_header.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if("parameter", token.parameter_keyword, iCurrent, lObjects)

    if utils.is_next_token("(", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)
        iCurrent = formal_parameter_list.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("return", token.return_keyword, iToken, lObjects)
    iCurrent = type_mark.classify(iCurrent, lObjects)

    return iCurrent
