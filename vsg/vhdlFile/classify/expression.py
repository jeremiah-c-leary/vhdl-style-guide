# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.vhdlFile.classify import (
    bit_string_literal,
    character_literal,
    external_name,
    utils,
)


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure, oType=parser.todo):
    """
    expression ::=
        condition_operator primary
      | logical_expression
    """
    iParen = 0
    while oDataStructure.advance_to_next_token():
        iParen = update_paren_counter(iParen, oDataStructure)

        if utils.unmatched_close_paren_found(iParen):
            break

        if oDataStructure.get_current_token_lower_value() in lUntils:
            if utils.is_current_token_close_paren(oDataStructure):
                oDataStructure.replace_current_token_with(parser.close_parenthesis)
                oDataStructure.increment_current_index()
            elif oDataStructure.current_token_lower_value_is(","):
                if iParen == 0:
                    break
                else:
                    oDataStructure.replace_current_token_with(parser.comma)
            else:
                break
        else:
            if external_name.detect(oDataStructure):
                continue
            elif bit_string_literal.detect(oDataStructure):
                continue
            elif character_literal.detect(oDataStructure):
                continue

            utils.assign_special_tokens(oDataStructure, oType)


@decorators.print_classifier_debug_info(__name__)
def update_paren_counter(iParen, oDataStructure):
    if utils.is_current_token_open_paren(oDataStructure):
        return iParen + 1
    elif utils.is_current_token_close_paren(oDataStructure):
        return iParen - 1
    return iParen
