# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import subprogram_instantiation_declaration as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import generic_map_aspect, signature, subprogram_kind


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    subprogram_instantiation_declaration ::=
        subprogram_kind identifier is new uninstantiated_subprogram_name [ signature ]
            [ generic_map_aspect ] ;
    """

    if subprogram_kind.detect(oDataStructure):
        if oDataStructure.does_string_exist_in_next_n_tokens("is", 3):
            if oDataStructure.does_string_exist_in_next_n_tokens("new", 4):
                classify(oDataStructure)
                return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    subprogram_kind.classify(oDataStructure)

    oDataStructure.replace_next_token_with(token.identifier)
    oDataStructure.replace_next_token_required("is", token.is_keyword)
    oDataStructure.replace_next_token_required("new", token.new_keyword)
    oDataStructure.replace_next_token_with(token.uninstantiated_subprogram_name)

    signature.detect(oDataStructure)

    generic_map_aspect.detect(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
