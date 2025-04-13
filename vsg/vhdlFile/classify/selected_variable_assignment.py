# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import selected_variable_assignment as token
from vsg.vhdlFile.classify import expression, selected_expressions, utils


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
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("with", token.with_keyword)

    expression.classify_until(["select"], oDataStructure)

    oDataStructure.replace_next_token_required("select", token.select_keyword)

    oDataStructure.replace_next_token_with_if("?", token.question_mark)

    utils.assign_tokens_until(":=", token.target, oDataStructure)

    oDataStructure.replace_next_token_required(":=", token.assignment)

    selected_expressions.classify_until([";"], oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
