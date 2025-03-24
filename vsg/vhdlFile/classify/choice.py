# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import choice as token
from vsg.vhdlFile import utils


@decorators.print_classifier_debug_info(__name__)
def classify_until(lUntils, oDataStructure):
    """
    choice ::=
        simple_expression
      | discrete_range
      | *element*_simple_name
      | **others**
    """
    if oDataStructure.is_next_token("others"):
        oDataStructure.replace_next_token_with(token.others_keyword)
    else:
        while not oDataStructure.is_next_token_one_of(lUntils):
            oDataStructure.replace_next_token_with(parser.todo)


# TODO:  Need to watch out for parenthesis in lUntils
#    iParen = 0
#    for iIndex in range(iToken, len(lObjects)):
#        iParen = utils.update_paren_counter(iIndex, lObjects, iParen)
#        if utils.is_next_token_in_list(lUntils, iIndex, lObjects) and iParen == 0:
#            return iIndex
#        if utils.is_item(lObjects, iIndex):
#            if utils.is_next_token("others", iIndex, lObjects):
#                utils.assign_next_token_required("others", token.others_keyword, iIndex, lObjects)
#            else:
#                utils.assign_next_token(parser.todo, iIndex, lObjects)
#
#    return iToken
