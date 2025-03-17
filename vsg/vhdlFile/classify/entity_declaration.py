# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import entity_declaration as token
from vsg.vhdlFile.classify import (
    entity_declarative_part,
    entity_header,
    entity_statement_part,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    entity_declaration ::=
        entity identifier is
            entity_header
            entity_declarative_part
        [ begin
            entity_statement_part ]
        end [ entity ] [ entity_simple_name ] ;
    """

    if oDataStructure.is_next_token("entity"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_current_token_with(token.entity_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("is", token.is_keyword)

    entity_header.detect(oDataStructure)

    entity_declarative_part.detect(oDataStructure)

    if oDataStructure.is_next_token("begin"):
        oDataStructure.replace_current_token_with(token.begin_keyword)
        entity_statement_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)
    oDataStructure.replace_next_token_with_if("entity", token.end_entity_keyword)
    oDataStructure.replace_next_token_with_if_not(";", token.entity_simple_name)
    oDataStructure.replace_next_token_required(";", token.semicolon)
