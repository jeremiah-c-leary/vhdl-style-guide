
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_line_preceeding_line(iLine, lAllTokens, iNumLines, oTokenMap):
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    iAdjust = -2
    iStart = lCarriageReturns[iLine - iNumLines + iAdjust] + 1
    iEnd = lCarriageReturns[iLine + iAdjust]
    lTemp = lAllTokens[iStart:iEnd]

    return tokens.New(iStart, iLine, lTemp)
