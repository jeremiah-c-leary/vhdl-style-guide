# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subtype_declaration as token
from vsg.vhdlFile.classify import identifier, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subtype_declaration ::=
        subtype identifier is subtype_indication ;
    """

    if oDataStructure.is_next_seek_token("subtype"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("subtype", token.subtype_keyword)

    identifier.classify(oDataStructure, token.identifier)

    oDataStructure.replace_next_token_required("is", token.is_keyword)

    subtype_indication.classify(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
