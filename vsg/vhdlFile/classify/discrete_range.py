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
    oDataStructure.push_seek_index()

    if oDataStructure.are_next_consecutive_tokens([None, "(", None, ")"], False):
        oDataStructure.pop_seek_index()
        oDataStructure.push_current_index()
        oDataStructure.iCurrent = oDataStructure.iSeek

        subtype_indication.classify(oDataStructure)

        oDataStructure.pop_current_index()
        return True

    oDataStructure.pop_seek_index()
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

    while not oDataStructure.at_end_of_file():
        oDataStructure.advance_to_next_token()

        if oDataStructure.current_token_lower_value_is("("):
            iOpenParenthesis += 1
        elif oDataStructure.current_token_lower_value_is(")"):
            iCloseParenthesis += 1

        if iOpenParenthesis < iCloseParenthesis:
            break
        elif iOpenParenthesis == iCloseParenthesis:
            if oDataStructure.is_next_token_one_of(lUntils):
                break
            else:
                oDataStructure.replace_current_token_with(parser.todo)
        else:
            oDataStructure.replace_current_token_with(parser.todo)
