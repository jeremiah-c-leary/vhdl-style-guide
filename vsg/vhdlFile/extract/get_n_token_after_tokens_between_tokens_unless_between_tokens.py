# -*- coding: utf-8 -*-

from vsg.vhdlFile.extract import tokens, utils


def get_n_token_after_tokens_between_tokens_unless_between_tokens(iToken, lTokens, oStart, oEnd, lUnless, lAllTokens, oTokenMap):
    lReturn = []

    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lIndexes = []
    for iStart, iEnd in zip(lStart, lEnd):
        for oToken in lTokens:
            lTemp = oTokenMap.get_token_indexes_between_indexes(oToken, iStart, iEnd)
            for iTemp in lTemp:
                iTokenIndex = iTemp
                for iCount in range(0, iToken):
                    iTokenIndex = oTokenMap.get_index_of_next_non_whitespace_token(iTokenIndex, bExcludeComments=True)
                lIndexes.append(iTokenIndex)

    lIndexes.sort()
    lIndexes = utils.filter_indexes_in_unless_regions(lIndexes, lUnless, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))

    return lReturn
