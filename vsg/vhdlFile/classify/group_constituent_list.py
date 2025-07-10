# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import group_constituent_list as token


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    group_constituent_list ::=
        group_constituent { , group_constituent }
    """
    oDataStructure.replace_next_token_with(token.group_constituent)

    while oDataStructure.is_next_token(","):
        oDataStructure.replace_next_token_with(token.comma)
        oDataStructure.replace_next_token_with(token.group_constituent)
