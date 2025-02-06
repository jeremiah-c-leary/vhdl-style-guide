# -*- coding: utf-8 -*-

from vsg.token import identifier as token


def classify(oDataStructure, oType=token.identifier):
    """
    identifier ::=
        basic_identifier | extended_identifier
    """

    oDataStructure.replace_next_token_with(oType)
