# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subprogram_body as token
from vsg.vhdlFile.classify import (
    subprogram_declarative_part,
    subprogram_kind,
    subprogram_statement_part,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_body ::=
        subprogram_specification is
            subprogram_declarative_part
        begin
            subprogram_statement_part
        end [ subprogram_kind ] [ designator ] ;
    """

    if oDataStructure.is_next_token("is"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.is_keyword)

    subprogram_declarative_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("begin", token.begin_keyword)

    subprogram_statement_part.detect(oDataStructure)

    oDataStructure.replace_next_token_required("end", token.end_keyword)

    if subprogram_kind.detect(oDataStructure):
        subprogram_kind.classify(oDataStructure)

    oDataStructure.replace_next_token_with_if_not(";", token.designator)
    oDataStructure.replace_next_token_required(";", token.semicolon)
