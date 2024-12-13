# -*- coding: utf-8 -*-

from vsg.vhdlFile.extract import tokens, utils


def get_tokens_matching_in_range_bounded_by_tokens_unless_between_tokens(lTokens, oStart, oEnd, lUnless, lAllTokens, oTokenMap):
    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lIndexes = []
    for iStart, iEnd in zip(lStart, lEnd):
        for oToken in lTokens:
            lIndexes.extend(oTokenMap.get_token_indexes_between_indexes(oToken, iStart, iEnd))

    lIndexes.sort()
    lIndexes = utils.filter_indexes_in_unless_regions(lIndexes, lUnless, oTokenMap)

    lReturn = []
    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))

    return lReturn
