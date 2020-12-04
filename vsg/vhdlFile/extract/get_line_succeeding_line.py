
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_line_succeeding_line(iLine, lAllTokens, iNumLines, oTokenMap):
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)

    iStart = lCarriageReturns[iLine - 1] + 1
    try:
        iEnd = lCarriageReturns[iLine + iNumLines - 1]

        lTemp = lAllTokens[iStart:iEnd]

        return tokens.New(iStart, iLine + 1, lTemp)
    except IndexError:
        return None
