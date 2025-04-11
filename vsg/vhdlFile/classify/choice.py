# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import choice as token


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
