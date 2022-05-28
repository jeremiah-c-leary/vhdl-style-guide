
from vsg import parser

from vsg.vhdlFile.extract import tokens

import bisect


def get_line_number(iLine, lAllTokens, iNumLines, oTokenMap, bSkipComments=False):

    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    iAdjust = -1
    iStartIndex = iLine - iNumLines + iAdjust
    if iStartIndex < 0:
        iStart = 0
    else:
        iStart = lCarriageReturns[iStartIndex] + 1
    iEnd = lCarriageReturns[iLine + iAdjust] + 1
    lTemp = lAllTokens[iStart:iEnd]
#    print(f'{iLine} | {iStart} | {iEnd} | {lTemp}')
    return tokens.New(iStart, iLine, lTemp)
