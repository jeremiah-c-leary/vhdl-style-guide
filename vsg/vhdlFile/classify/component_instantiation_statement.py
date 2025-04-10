# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import component_instantiation_statement as token
from vsg.vhdlFile.classify import (
    generic_map_aspect,
    instantiated_unit,
    port_map_aspect,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    component_instantiation_statement ::=
        instantiation_label :
            instantiated_unit
                [ generic_map_aspect ]
                [ port_map_aspect ] ;
    """
    if oDataStructure.are_next_consecutive_tokens([None, ":"]):
        oDataStructure.advance_to_next_seek_token()
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()
        if instantiated_unit.detect(oDataStructure):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    utils.tokenize_label(oDataStructure, token.instantiation_label, token.label_colon)

    instantiated_unit.classify(oDataStructure)

    generic_map_aspect.detect(oDataStructure)

    port_map_aspect.detect(oDataStructure)

    oDataStructure.replace_next_token_required(";", token.semicolon)
