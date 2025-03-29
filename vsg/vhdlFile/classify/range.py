# -*- coding: utf-8 -*-

from vsg import decorators
from vsg.vhdlFile.classify import attribute_name


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    range ::=
        *range*_attribute_name
      | simple_expression direction simple_expression
    """
    if oDataStructure.are_next_consecutive_tokens(["(", None, ")"]):
        return True
    # TODO:  move mySeek into oDataStructure
    mySeek = oDataStructure.iSeek
    if attribute_name.detect(oDataStructure):
        return True
    oDataStructure.iSeek = mySeek
    return detect_direction(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def detect_direction(oDataStructure):
    #    oDataStructure.align_seek_index()
    if oDataStructure.does_string_exist_before_matching_close_parenthesis("downto", 0):
        return True
    if oDataStructure.does_string_exist_before_matching_close_parenthesis("to", 0):
        return True
    return False
