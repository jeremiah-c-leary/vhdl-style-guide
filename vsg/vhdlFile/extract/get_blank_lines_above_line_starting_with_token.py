
from vsg import parser

from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_blank_lines_above_line_starting_with_token(lTokens, lAllTokens, oTokenMap):

    lReturn = []

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)
    lBlankLines = oTokenMap.get_token_indexes(parser.blank_line)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iEnd = lCarriageReturns[iLine - 2]
        for i in range(iLine - 3, 0, -1):
            iCarriageReturnIndex = lCarriageReturns[i]
            if not iCarriageReturnIndex + 1 in lBlankLines:
                iStart = lCarriageReturns[i + 1]
                if iStart != iEnd:
                    lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart:iEnd]))
                break

    return lReturn
