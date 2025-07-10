# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import architecture_body as token
from vsg.vhdlFile.classify import (
    architecture_declarative_part,
    architecture_statement_part,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    architecture identifier of *entity*_name is
        architecture_declarative_part
    begin
        architecture_statement_part
    end [ architecture ] [ *architecture*_simple_name ] ;
    """

    if oDataStructure.is_next_token("architecture"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.architecture_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("of", token.of_keyword)
    oDataStructure.replace_next_token_with(token.entity_name)
    oDataStructure.replace_next_token_required("is", token.is_keyword)

    architecture_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("begin", token.begin_keyword)

    architecture_statement_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_with_if("architecture", token.end_architecture_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.architecture_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
