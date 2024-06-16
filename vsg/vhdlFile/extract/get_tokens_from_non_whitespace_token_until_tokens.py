# -*- coding: utf-8 -*-

from vsg.vhdlFile.extract import tokens


def get_tokens_from_non_whitespace_token_until_tokens(lTokens, lAllTokens, oTokenMap):
    lReturn = []
    lIndexPairs = []

    for oToken in lTokens:
        for iTokenIndex in oTokenMap.get_token_indexes(oToken):
            iPreviousIndex = oTokenMap.get_index_of_previous_non_whitespace_token(iTokenIndex)
            lIndexPairs.append([iPreviousIndex, iTokenIndex])

    for lIndex in lIndexPairs:
        iStart = lIndex[0]
        iEnd = lIndex[1]
        iLine = oTokenMap.get_line_number_of_index(iEnd)
        lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart:iEnd]))

    return lReturn
