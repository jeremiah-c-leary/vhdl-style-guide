# -*- coding: utf-8 -*-
import copy

from vsg import decorators, parser
from vsg.token import sensitivity_list as token
from vsg.vhdlFile.classify import name, utils


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    """
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    """

    iParen = 0
    while oDataStructure.advance_to_next_token():
        iParen = utils.update_paren_counter(iParen, oDataStructure)

        if utils.unmatched_close_paren_found(iParen):
            break

        if oDataStructure.is_next_token(","):
            oDataStructure.replace_next_token_with(token.comma)
        else:
            name.classify_until([","], oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    sensitivity_list ::=
        *signal*_name { , *signal*_name}
    """
    lMyUntils = copy.deepcopy(lUntils)
    lMyUntils.append(",")
    while not oDataStructure.is_next_token_one_of(lUntils):
        oDataStructure.replace_next_token_with_if(",", token.comma)
        name.classify_until(lMyUntils, oDataStructure)
