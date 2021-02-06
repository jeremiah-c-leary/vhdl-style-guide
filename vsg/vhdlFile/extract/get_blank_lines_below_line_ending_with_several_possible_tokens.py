
from vsg import parser

from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_blank_lines_below_line_ending_with_several_possible_tokens(lTokens, lAllTokens, oTokenMap):

    lReturn = []

    lIndexes = utils.get_indexes_of_tokens_between(lTokens[0], lTokens[1:], oTokenMap)

    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)
    lBlankLines = oTokenMap.get_token_indexes(parser.blank_line)

    for iIndex in lIndexes:
        if not utils.is_token_at_end_of_line(iIndex, oTokenMap):
            continue
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


