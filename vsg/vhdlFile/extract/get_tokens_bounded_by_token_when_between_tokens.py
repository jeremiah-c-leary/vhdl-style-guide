
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_bounded_by_token_when_between_tokens(oLeft, oRight, oStart, oEnd, lAllTokens, oTokenMap, include_trailing_whitespace=False):

    lLeft, lRight = oTokenMap.get_token_pair_indexes(oLeft, oRight)
    lStart, lEnd = oTokenMap.get_token_pair_indexes(oStart, oEnd)
    lReturn = []
    for iStart, iEnd in zip(lStart, lEnd):
        for iLeft, iRight in zip(lLeft, lRight):
            if iStart < iLeft and iRight < iEnd:
                iLine = oTokenMap.get_line_number_of_index(iLeft)
                if include_trailing_whitespace:
                    if oTokenMap.is_token_at_index(iRight + 1, parser.whitespace):
                        lReturn.append(tokens.New(iLeft, iLine, lAllTokens[iLeft:iRight + 2]))
                    else:
                        lReturn.append(tokens.New(iLeft, iLine, lAllTokens[iLeft:iRight + 1]))
                else:
                    lReturn.append(tokens.New(iLeft, iLine, lAllTokens[iLeft:iRight + 1]))
    return lReturn
