# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import range, subtype_indication


@decorators.print_classifier_debug_info(__name__)
def detect(oDataStructure):
    """
    discrete_range ::=
        *discrete*_subtype_indication | range
    """
    if oDataStructure.are_next_consecutive_tokens([None, "(", None, ")"]):
        subtype_indication.classify(oDataStructure)
        return True
    return range.detect(oDataStructure)


@decorators.print_classifier_debug_info(__name__)
def classify(iToken, lObjects):
    """
    discrete_range ::=
        *discrete*_subtype_indication | range
    """

    return utils.assign_token(lObjects, iToken, parser.todo)


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    iOpenParenthesis = 0
    iCloseParenthesis = 0

    while not oDataStructure.is_next_token_one_of(lUntils):
        #        if iCurrent == iPrevious:
        #            utils.print_missing_error_message(lUntils, iToken, lObjects)

        if oDataStructure.current_token_lower_value_is("("):
            iOpenParenthesis += 1
        elif oDataStructure.current_token_lower_value_is(")"):
            iCloseParenthesis += 1
        if iOpenParenthesis < iCloseParenthesis:
            break
        else:
            oDataStructure.replace_current_token_with(parser.todo)
