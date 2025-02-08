# -*- coding: utf-8 -*-

from vsg.token import identifier_list as token


def classify_until(lUntils, oDataStructure, oToken=token.identifier):
    """
    identifier_list ::=
        identifier { , identifier }
    """

    while not oDataStructure.is_next_token_one_of(lUntils):
        oDataStructure.replace_next_token_with_if_not(",", oToken)
        oDataStructure.replace_next_token_with_if(",", token.comma)
