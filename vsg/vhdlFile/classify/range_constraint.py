# -*- coding: utf-8 -*-

from vsg import decorators, parser
from vsg.token import range_constraint as token
from vsg.vhdlFile.classify import utils


@decorators.print_classifier_debug_info(__name__)
@decorators.push_pop_seek_index
def detect(oDataStructure):
    """
    range_constraint ::=
        **range** range
    """

    if oDataStructure.is_next_token("range"):
        classify(oDataStructure)
        return True
    return False


@decorators.print_classifier_debug_info(__name__)
def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.range_keyword)

    # TODO:  Refactor the following into the data structure
    iParenCnt = 0
    while not oDataStructure.is_next_token_one_of([";", "units", ":="]):
        iParenCnt = utils.update_paren_counter(iParenCnt, oDataStructure)
        if iParenCnt == -1:
            break
        oDataStructure.replace_current_token_with(parser.todo)
