# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import block_statement as token
from vsg.vhdlFile.classify import (
    block_declarative_part,
    block_header,
    block_statement_part,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    block_statement ::=
    block_label :
        block [ ( *guard*_condition ) ] [ is ]
            block_header
            block_declarative_part
        begin
            block_statement_part
        end block [ block_label ] ;
    """

    if oDataStructure.are_next_consecutive_tokens([None, ":", "block"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.block_label, token.label_colon)
    oDataStructure.replace_next_token_with(token.block_keyword)

    if oDataStructure.is_next_token("("):
        oDataStructure.replace_next_token_with(token.guard_open_parenthesis)
        oDataStructure.replace_next_token_with_if_not(")", token.guard_condition)
        oDataStructure.replace_next_token_required(")", token.guard_close_parenthesis)

    oDataStructure.replace_next_token_with_if("is", token.is_keyword)

    block_header.detect(oDataStructure)

    block_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("begin", token.begin_keyword)

    block_statement_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_required("block", token.end_block_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.end_block_label)
    oDataStructure.replace_next_token_required(";", token.semicolon)
