# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import incomplete_type_declaration as token
from vsg.vhdlFile.classify import identifier


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    incomplete_type_declaration ::=
        type identifier ;
    """
    if oDataStructure.are_next_consecutive_tokens(["type", None, ";"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("type", token.type_keyword)

    identifier.classify(oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required(";", token.semicolon)
