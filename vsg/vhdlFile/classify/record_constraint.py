# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.token import record_constraint as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import record_element_constraint


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    record_constraint ::=
        ( record_element_constraint { , record_element_constraint } )
    """
    oDataStructure.align_seek_index()
    if oDataStructure.is_next_seek_token("("):
        oDataStructure.increment_seek_index()
        if record_element_constraint.detect(oDataStructure):
            classify(oDataStructure)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_required("(", token.open_parenthesis)

    while not oDataStructure.is_next_token(")"):

        record_element_constraint.classify(oDataStructure)
        oDataStructure.replace_next_token_with_if(",", token.comma)
    oDataStructure.replace_next_token_required(")", token.close_parenthesis)
