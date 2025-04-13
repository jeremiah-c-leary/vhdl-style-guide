# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import record_element_constraint as token
from vsg.vhdlFile.classify import element_constraint


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    record_element_constraint ::=
        record_element_simple_name element_constraint
    """

    if not oDataStructure.is_next_seek_token("("):
        oDataStructure.increment_seek_index()
        if oDataStructure.is_next_seek_token("("):
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.record_element_simple_name)
    element_constraint.detect(oDataStructure)
