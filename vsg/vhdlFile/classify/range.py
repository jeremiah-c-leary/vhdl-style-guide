# -*- coding: utf-8 -*-

from vsg.vhdlFile.classify import attribute_name


def detect(oDataStructure):
    """
    range ::=
        *range*_attribute_name
      | simple_expression direction simple_expression
    """
    if attribute_name.detect(oDataStructure):
        return True
    return detect_direction(oDataStructure)


def detect_direction(oDataStructure):
    if oDataStructure.does_string_exist_before_matching_close_parenthesis("downto"):
        return True
    if oDataStructure.does_string_exist_before_matching_close_parenthesis("to"):
        return True
    return False
