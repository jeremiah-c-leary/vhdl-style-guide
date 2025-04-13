# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import interface_subprogram_default as token


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    interface_subprogram_default ::=
        *subprogram*_name | <>
    """

    if oDataStructure.is_next_token("<>"):
        oDataStructure.replace_next_token_with(token.undefined_range)
    else:
        oDataStructure.replace_next_token_with(token.subprogram_name)
