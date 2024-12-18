# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import attribute_name as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import expression, signature


def detect(iToken, lObjects):
    """
    attribute_name ::=
        prefix [ signature ] ' attribute_designator [ ( expression ) ]
    """

    # Skip over prefix
    iCurrent = utils.find_next_token(iToken, lObjects)
    iCurrent = utils.find_next_token(iCurrent + 1, lObjects)

    if utils.token_is_open_parenthesis(iCurrent, lObjects):
        iCurrent += 1
        iCurrent = utils.skip_tokens_until_matching_closing_paren(iCurrent, lObjects)
        iCurrent += 1

    # Check for signature
    if utils.is_next_token("[", iCurrent, lObjects):
        return True

    # Check for tic
    if utils.is_next_token("'", iCurrent, lObjects):
        return True

    return False


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token(token.name, iToken, lObjects)
    iCurrent = utils.find_next_token(iCurrent, lObjects)

    if utils.token_is_open_parenthesis(iCurrent, lObjects):
        iCurrent = utils.assign_token(lObjects, iCurrent, parser.open_parenthesis)
        iCurrent = utils.assign_tokens_until_matching_closing_paren(parser.todo, iCurrent, lObjects)
        iCurrent = utils.assign_token(lObjects, iCurrent, parser.close_parenthesis)

    signature.detect(iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("'", token.tic, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.attribute, iCurrent, lObjects)

    return iCurrent
