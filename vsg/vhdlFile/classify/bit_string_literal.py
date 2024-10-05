# -*- coding: utf-8 -*-


from vsg.token import bit_string_literal as token
from vsg.vhdlFile import utils

sIntegerPattern = r"^\d+$"
sBaseSpecifierPattern = r"^(([us]?[box])|d)$"
sBitValueStringPattern = r"^\"[0-9a-fhluwxz\-_]*\"$"


def detect(iToken, lObjects):
    """
    bit_string_literal ::=
        [ integer ] base_specifier " [ bit_value ] "
    """

    iCurrent = utils.find_next_token(iToken, lObjects)
    if utils.matches_next_token(sIntegerPattern, iToken, lObjects):
        iCurrent += 1
    if utils.matches_next_token(sBaseSpecifierPattern, iCurrent, lObjects):
        iCurrent = utils.find_next_token(iCurrent, lObjects)
        iCurrent += 1
        if utils.matches_next_token(sBitValueStringPattern, iCurrent, lObjects):
            return classify(iToken, lObjects)
    return iToken


def classify(iToken, lObjects):
    if utils.matches_next_token(sIntegerPattern, iToken, lObjects):
        iCurrent = utils.assign_next_token(token.integer, iToken, lObjects)
    else:
        iCurrent = iToken
    iCurrent = utils.assign_next_token(token.base_specifier, iCurrent, lObjects)
    iCurrent = utils.assign_next_token(token.bit_value_string, iCurrent, lObjects)
    return iCurrent
