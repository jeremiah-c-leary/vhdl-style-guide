# -*- coding: utf-8 -*-

from vsg.vhdlFile.extract import tokens, utils


def get_sequence_of_tokens_matching(lTokens, lAllTokens, oTokenMap, bIgnoreIfLineStart=False):
    lReturn = []

    lIndexes = get_token_indexes(lTokens, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        if bIgnoreIfLineStart and utils.is_token_at_start_of_line(iIndex, oTokenMap):
            continue
        for iToken, oToken in enumerate(lTokens):
            if not isinstance(lAllTokens[iToken + iIndex], oToken):
                break
        else:
            lReturn.append(tokens.New(iIndex, iLine, lAllTokens[iIndex : iIndex + len(lTokens)]))

    return lReturn


def get_token_indexes(lTokens, oTokenMap):
    lIndexes = oTokenMap.get_token_indexes(lTokens[0])
    if len(lIndexes) > 0:
        return lIndexes

    lTemp = oTokenMap.get_token_indexes(lTokens[-1])
    iAdjust = len(lTokens) - 1
    for iIdx, iTemp in enumerate(lTemp):
        iNewIdx = iTemp - iAdjust
        lIndexes.append(iNewIdx)
    return lIndexes
