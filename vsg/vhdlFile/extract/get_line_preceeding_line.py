
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_line_preceeding_line(iLine, lAllTokens, iNumLines, oTokenMap):
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    iAdjust = -2
    iStartIndex = iLine - iNumLines + iAdjust
    if iStartIndex < 0:
        iStart = 0
    else:
        iStart = lCarriageReturns[iStartIndex] + 1
    iEnd = lCarriageReturns[iLine + iAdjust]
    lTemp = lAllTokens[iStart:iEnd]
#    print(f'{iLine} | {iStart} | {iEnd} | {lTemp}')
    return tokens.New(iStart, iLine, lTemp)
