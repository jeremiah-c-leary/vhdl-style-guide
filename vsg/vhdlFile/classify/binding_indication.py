# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import binding_indication as token
from vsg.vhdlFile.classify import entity_aspect, generic_map_aspect, port_map_aspect


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    binding_indication ::=
        [ **use** entity_aspect ]
        [ generic_map_aspect ]
        [ port_map_aspect ]
    """
    if oDataStructure.is_next_token_one_of(["use", "generic", "port"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    if oDataStructure.is_next_token("use"):
        oDataStructure.replace_next_token_with(token.use_keyword)
        entity_aspect.classify(oDataStructure)

    generic_map_aspect.detect(oDataStructure)

    port_map_aspect.detect(oDataStructure)
