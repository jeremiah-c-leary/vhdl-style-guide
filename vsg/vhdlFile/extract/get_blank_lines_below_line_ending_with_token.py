
from vsg import parser

from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_blank_lines_below_line_ending_with_token(lTokens, lAllTokens, oTokenMap):

    lReturn = []

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)
    lBlankLines = oTokenMap.get_token_indexes(parser.blank_line)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iStart = lCarriageReturns[iLine - 1] + 1
        for i in range(iLine - 1, len(lCarriageReturns)):
            iCarriageReturnIndex = lCarriageReturns[i]
            if not iCarriageReturnIndex + 1 in lBlankLines:
                iEnd = lCarriageReturns[i] + 1
                lTemp = lAllTokens[iStart:iEnd]
                if len(lTemp) > 0:
                    lReturn.append(tokens.New(iStart, iLine, lTemp))
                break

    return lReturn
