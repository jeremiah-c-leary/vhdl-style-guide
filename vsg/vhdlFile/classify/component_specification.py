# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import component_specification as token
from vsg.vhdlFile.classify import instantiation_list


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    component_specification ::=
        instantiation_list : component_name
    """

    while oDataStructure.does_string_exist_in_next_n_tokens_from_seek_index(",", 2):
        oDataStructure.increment_seek_index()

    if oDataStructure.does_string_exist_in_next_n_tokens_from_seek_index(":", 2):
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    instantiation_list.classify(oDataStructure)

    oDataStructure.replace_next_token_required(":", token.colon)
    oDataStructure.replace_next_token_with(token.component_name)
