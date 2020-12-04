
from vsg import parser

from vsg.vhdlFile.extract import tokens


def get_tokens_from_line(iLineNumber, lAllTokens, oTokenMap):
    lIndexes = oTokenMap.get_token_indexes(parser.carriage_return)
    iLine = iLineNumber - 2

    iStart = lIndexes[iLine] + 1
    iEnd = lIndexes[iLine + 1] + 1

    lTemp = lAllTokens[iStart:iEnd]

    return tokens.New(iStart, iLineNumber, lTemp)
