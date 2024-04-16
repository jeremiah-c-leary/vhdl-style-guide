# -*- coding: utf-8 -*-

from vsg.token import subprogram_body as token
from vsg.vhdlFile.extract.get_tokens_bounded_by import get_tokens_bounded_by

oStart = token.is_keyword
oEnd = token.begin_keyword


def extract(lAllTokens, oTokenMap):
    lReturn = []
    iStart = 1
    lToi = get_tokens_bounded_by(oStart, oEnd, lAllTokens, oTokenMap)
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        iEnd = len(lTokens) - 1
        lReturn.append(oToi.extract_tokens(iStart, iEnd))
    return lReturn
