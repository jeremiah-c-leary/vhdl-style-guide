# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import range_constraint as token
from vsg.vhdlFile.classify import utils


def detect(oDataStructure):
    """
    range_constraint ::=
        **range** range
    """
    if oDataStructure.is_next_token("range"):
        classify(oDataStructure)
        return True
    return False


def classify(oDataStructure):
    oDataStructure.replace_next_token_with(token.range_keyword)

    iParenCnt = 0
    while not oDataStructure.is_next_token_one_of([";", "units", ":="]):
        iParenCnt = utils.update_paren_counter(iParenCnt, oDataStructure)
        if iParenCnt == -1:
            break
        oDataStructure.replace_next_token_with(parser.todo)
        oDataStructure.increment_current_index()
