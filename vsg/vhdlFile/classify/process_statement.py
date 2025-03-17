# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import process_statement as token
from vsg.vhdlFile.classify import (
    process_declarative_part,
    process_sensitivity_list,
    process_statement_part,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    process_statement ::=
        [ *process*_label : ]
            [ postponed ] process [ ( process_sensitivity_list ) ] [ is ]
                process_declarative_part
            begin
                process_statement_part
            end [ postponed ] process [ *process*_label ] ;
    """
    if oDataStructure.does_string_exist_in_next_n_tokens("process", 4):
        if not oDataStructure.does_string_exist_in_next_n_tokens(";", 3):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    classify_opening_declaration(oDataStructure)

    process_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("begin", token.begin_keyword)

    process_statement_part.detect(oDataStructure)

    classify_closing_declaration(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify_opening_declaration(oDataStructure):
    utils.tokenize_label(oDataStructure, token.process_label, token.label_colon)
    oDataStructure.replace_next_token_with_if("postponed", token.postponed_keyword)
    oDataStructure.replace_next_token_required("process", token.process_keyword)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(token.open_parenthesis)
        process_sensitivity_list.classify(oDataStructure)
        oDataStructure.replace_next_token_required(")", token.close_parenthesis)

    oDataStructure.replace_next_token_with_if("is", token.is_keyword)


@decorators.print_classifier_debug_info(__name__)
def classify_closing_declaration(oDataStructure):
    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_with_if("postponed", token.end_postponed_keyword)
    oDataStructure.replace_next_token_required("process", token.end_process_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_process_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)
