# -*- coding: utf-8 -*-

from vsg import parser
from vsg.vhdlFile.extract import tokens


def get_tokens_matching_not_at_beginning_or_ending_of_line(lTokens, lAllTokens, oTokenMap):
    lReturn = []
    lIndexes = []
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    for oToken in lTokens:
        lIndexes.extend(oTokenMap.get_token_indexes(oToken))

    lIndexes.sort()

    for iIndex in lIndexes:
        if iIndex - 1 not in lCarriageReturns and iIndex + 1 not in lCarriageReturns:
            iLine = oTokenMap.get_line_number_of_index(iIndex)
            lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))

    return lReturn
