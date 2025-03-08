# -*- coding: utf-8 -*-

from vsg.token import selected_variable_assignment as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, selected_expressions
from vsg import decorators


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    selected_variable_assignment ::=
        with expression select [ ? ]
           target := selected_expressions ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string(":=", ";"):
        if oDataStructure.does_string_exist_before_string("with", ";"):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("with", token.with_keyword, iToken, lObjects)

    iCurrent = expression.classify_until(["select"], iToken, lObjects)

    iCurrent = utils.assign_next_token_required("select", token.select_keyword, iToken, lObjects)
    iCurrent = utils.assign_next_token_if("?", token.question_mark, iCurrent, lObjects)
    iCurrent = utils.assign_tokens_until(":=", token.target, iCurrent, lObjects)
    iCurrent = utils.assign_next_token_required(":=", token.assignment, iCurrent, lObjects)

    iCurrent = selected_expressions.classify_until([";"], iToken, lObjects)

    iCurrent = utils.assign_next_token_required(";", token.semicolon, iCurrent, lObjects)

    return iCurrent
