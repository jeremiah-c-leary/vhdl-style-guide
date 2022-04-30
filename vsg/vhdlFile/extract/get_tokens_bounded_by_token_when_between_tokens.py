
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by_token_when_between_tokens(oLeft, oRight, oStart, oEnd, lAllTokens, oTokenMap, include_trailing_whitespace=False):

    lMyPairs = get_token_pairs(oLeft, oRight, oStart, oEnd, oTokenMap)

    lReturn = []

    for lPair in lMyPairs:
        iLeft = lPair[0]
        iRight = lPair[1]
        iLine = oTokenMap.get_line_number_of_index(iLeft)
        if include_trailing_whitespace:
            if oTokenMap.is_token_at_index(iRight + 1, parser.whitespace):
                lReturn.append(tokens.New(iLeft, iLine, lAllTokens[iLeft:iRight + 2]))
            else:
                lReturn.append(tokens.New(iLeft, iLine, lAllTokens[iLeft:iRight + 1]))
        else:
            lReturn.append(tokens.New(iLeft, iLine, lAllTokens[iLeft:iRight + 1]))

    return lReturn


def get_token_pairs(oLeft, oRight, oStart, oEnd, oTokenMap):
    lLeft, lRight = oTokenMap.get_token_pair_indexes(oLeft, oRight)
    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)

    lPairs = keep_pairs_that_are_within_pairs(lLeft, lRight, lStart, lEnd)

    lReturn = remove_duplicate_pairs(lPairs)
    return lReturn


def keep_pairs_that_are_within_pairs(lLeft, lRight, lStart, lEnd):
    lPairs = []
    for iStart, iEnd in zip(lStart, lEnd):
        for iLeft, iRight in zip(lLeft, lRight):
            if iStart < iLeft and iRight < iEnd:
                lPairs.append([iLeft, iRight])
    return lPairs


def remove_duplicate_pairs(lPairs):
    lReturn = []
    for lPair in lPairs:
        if lPair not in lReturn:
            lReturn.append(lPair)
    return lReturn
