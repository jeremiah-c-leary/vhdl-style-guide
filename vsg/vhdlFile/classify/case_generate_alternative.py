# -*- coding: utf-8 -*-

from vsg.token import case_generate_alternative as token
from vsg.vhdlFile import utils
from vsg.vhdlFile.classify import choices, generate_statement_body


def detect(iToken, lObjects):
    """
    case_generate_alternative ::=
        when [ alternative_label : ] choices =>
            generate_statement_body
    """

    if utils.is_next_token("when", iToken, lObjects):
        return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token_required("when", token.when_keyword, iToken, lObjects)

    if utils.are_next_consecutive_tokens([None, ":"], iCurrent, lObjects):
        iCurrent = utils.assign_next_token(token.alternative_label_name, iCurrent, lObjects)
        iCurrent = utils.assign_next_token(token.alternative_label_colon, iCurrent, lObjects)

    iCurrent = choices.classify_until(["=>"], iCurrent, lObjects)

    iCurrent = utils.assign_next_token_required("=>", token.assignment, iCurrent, lObjects)

    iCurrent = generate_statement_body.classify(iCurrent, lObjects)

    return iCurrent
