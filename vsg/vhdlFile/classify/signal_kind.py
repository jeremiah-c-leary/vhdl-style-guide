# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import signal_kind as token


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    signal_kind ::=
        register | bus
    """

    if oDataStructure.is_next_seek_token_one_of(["register", "bus"]):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with_if("register", token.register_keyword)
    oDataStructure.replace_next_token_with_if("bus", token.bus_keyword)
