# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import direction
from vsg.vhdlFile.classify import external_name, utils


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure, oType=parser.todo):
    """
      name ::=
              simple_name
            | operator_symbol
            | character_literal
            | selected_name
            | indexed_name
            | slice_name
            | attribute_name
            | external_name

    NOTE: At the moment, everything will be set to parser.todo.
    """

    if external_name.detect(oDataStructure):
        return None

    iParen = 0
    while oDataStructure.advance_to_next_token():
        iParen = utils.update_paren_counter(iParen, oDataStructure)

        if utils.unmatched_close_paren_found(iParen):
            break

        if oDataStructure.get_current_token_lower_value() in lUntils:
            break
        else:
            utils.assign_special_tokens(oDataStructure, oType)
