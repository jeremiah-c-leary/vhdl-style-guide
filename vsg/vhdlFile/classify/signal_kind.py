# -*- coding: utf-8 -*-

from vsg.token import signal_kind as token


def detect(oDataStructure):
    """
    signal_kind ::=
        register | bus
    """
    oDataStructure.align_seek_index()
    if oDataStructure.is_next_seek_token_one_of(["register", "bus"]):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("register", token.register_keyword)
    oDataStructure.replace_next_token_with_if("bus", token.bus_keyword)
