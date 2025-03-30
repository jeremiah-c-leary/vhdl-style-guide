# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import selected_force_assignment as token
from vsg.vhdlFile.classify import expression, force_mode, selected_expressions, utils


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    selected_force_assignment ::= [§ 10.5.4]
        with expression select [ ? ]
            target <= force [ force_mode ] selected_expressions ;
    """

    if oDataStructure.is_next_token_one_of(["when", "if", "elsif", "else"]):
        return False
    if oDataStructure.does_string_exist_before_string("<=", ";"):
        if oDataStructure.does_string_exist_before_string("force", ";"):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("with", token.with_keyword)

    expression.classify_until(["select"], oDataStructure)

    oDataStructure.replace_next_token_required("select", token.select_keyword)
    oDataStructure.replace_next_token_with_if("?", token.question_mark)

    utils.assign_tokens_until("<=", token.target, oDataStructure)

    oDataStructure.replace_next_token_required("<=", token.assignment)
    oDataStructure.replace_next_token_required("force", token.force_keyword)

    force_mode.detect(oDataStructure)

    selected_expressions.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
