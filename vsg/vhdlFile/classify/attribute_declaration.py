# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import attribute_declaration as token
from vsg.vhdlFile.classify import type_mark


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    attribute_declaration ::=
        attribute identifier : type_mark ;
    """
    if oDataStructure.are_next_consecutive_tokens(["attribute", None, ":"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("attribute", token.attribute_keyword)
    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required(":", token.colon)

    type_mark.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
