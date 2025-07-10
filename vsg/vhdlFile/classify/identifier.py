# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import identifier as token


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure, oType=token.identifier):
    """
    identifier ::=
        basic_identifier | extended_identifier
    """

    oDataStructure.replace_next_token_with(oType)
