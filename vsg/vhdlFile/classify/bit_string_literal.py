# -*- coding: utf-8 -*-


from vsg import parser
from vsg.token import bit_string_literal as token
from vsg.vhdlFile import utils


def detect(iToken, lObjects):
    """
    bit_string_literal ::=
        [ integer ] base_specifier " [ bit_value ] "
    """

# XXX SUCCESS! We are parsing the bit_value and base specifier!
# TODO can we split the tokens up?

    if utils.matches_next_token(r"^\d*(([us]?[box])|d)$", iToken, lObjects):
        iCurrent = utils.find_next_token(iToken, lObjects)
        iCurrent += 1
        if utils.matches_next_token(r"^\"[0-9a-fhluwxz\-_]*\"$", iCurrent, lObjects):
            return classify(iToken, lObjects)

    return iToken

def classify(iToken, lObjects):
    iCurrent = utils.assign_next_token(token.base_specifier, iToken, lObjects)
    iCurrent = utils.assign_next_token(token.bit_value, iCurrent, lObjects)
    return iCurrent

# ["B", "O", "X", "UB", "UO", "UX", "SB", "SO", "SX", "D"]
