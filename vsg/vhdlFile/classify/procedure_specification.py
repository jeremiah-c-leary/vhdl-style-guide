# -*- coding: utf-8 -*-

from vsg.token import procedure_specification as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import formal_parameter_list, subprogram_header
from vsg import decorators


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
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("procedure", token.procedure_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.designator, iCurrent, lObjects)

    iCurrent = subprogram_header.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_if("parameter", token.parameter_keyword, iCurrent, lObjects)
    if utils.is_next_token("(", iCurrent, lObjects):
        iCurrent = utils.assign_next_token_required("(", token.open_parenthesis, iCurrent, lObjects)
        iCurrent = formal_parameter_list.classify(iCurrent, lObjects)
        iCurrent = utils.assign_next_token_required(")", token.close_parenthesis, iCurrent, lObjects)

    return iCurrent
