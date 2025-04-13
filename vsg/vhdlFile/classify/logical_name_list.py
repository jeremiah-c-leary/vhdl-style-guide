# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import logical_name_list as token


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    logical_name_list ::=
        logical_name { , logical_name }
    """
    while not oDataStructure.is_next_token_one_of(lUntils):
        oDataStructure.replace_next_token_with(token.logical_name)
        oDataStructure.replace_next_token_with_if(",", token.comma)
