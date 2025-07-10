# -*- coding: utf-8 -*-

from vsg import decorators, parser


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    character_literal ::=
        ' graphic_character '
    """
    oDataStructure.advance_to_next_seek_token()
    sValue = oDataStructure.get_seek_token_lower_value()
    if len(sValue) == 3 and sValue.startswith("'") and sValue.endswith("'"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(parser.character_literal)
