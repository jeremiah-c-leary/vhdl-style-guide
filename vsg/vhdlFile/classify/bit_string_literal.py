# -*- coding: utf-8 -*-

import re

from vsg import decorators
from vsg.token import bit_string_literal as token

oIntegerRegex = re.compile(r"\d+")
oBaseSpecifierRegex = re.compile(r"(([us]?[box])|d)")
oBitValueStringRegex = re.compile(r'"[0-9a-fhluwxz\-_]*"')


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    bit_string_literal ::=
        [ integer ] base_specifier " [ bit_value ] "
    """
    bInt = False
    if oDataStructure.does_seek_token_match_regex(oIntegerRegex):
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()
        bInt = True
    if oDataStructure.does_seek_token_match_regex(oBaseSpecifierRegex):
        oDataStructure.increment_seek_index()
        oDataStructure.advance_to_next_seek_token()

        if oDataStructure.does_seek_token_match_regex(oBitValueStringRegex):
            classify(oDataStructure, bInt)
            return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure, bInt):
    if bInt:
        oDataStructure.replace_next_token_with(token.integer)
    oDataStructure.replace_next_token_with(token.base_specifier)
    oDataStructure.replace_next_token_with(token.bit_value_string)
