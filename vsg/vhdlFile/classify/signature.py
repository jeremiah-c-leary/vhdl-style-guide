# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import signature as token
from vsg.vhdlFile.classify import type_mark


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    signature ::= **[** [ type_mark { , type_mark } ] [ return type_mark ] **]**

    NOTE:  The [ and ] enclosed by ** are required if the signature is provided.
    """

    return oDataStructure.is_next_seek_token("[")


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("[", token.open_bracket)

    detect_type_mark(oDataStructure)

    detect_return(oDataStructure)

    oDataStructure.replace_next_token_required("]", token.close_bracket)


@decorators.print_classifier_debug_info(__name__)
def detect_return(oDataStructure):
    if oDataStructure.is_next_seek_token("return"):
        oDataStructure.replace_next_token_with(token.return_keyword)
        type_mark.classify(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def detect_type_mark(oDataStructure):
    if not oDataStructure.is_next_seek_token("return"):
        type_mark.classify(oDataStructure)
        while oDataStructure.is_next_seek_token(","):
            oDataStructure.replace_next_token_required(",", token.comma)
            type_mark.classify(oDataStructure)
