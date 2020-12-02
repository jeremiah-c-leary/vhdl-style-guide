
from vsg import parser

from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_tokens_at_beginning_of_line_matching(lTokens, lAllTokens, oTokenMap):

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    lReturn = []
    for iIndex in lIndexes:
        if oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 1):
            iLine = oTokenMap.get_line_number_of_index(iIndex)
            lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))
        elif oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 2) and oTokenMap.is_token_at_index(parser.whitespace, iIndex - 1):
            iLine = oTokenMap.get_line_number_of_index(iIndex)
            lReturn.append(tokens.New(iIndex - 1, iLine, lAllTokens[iIndex - 1: iIndex + 1]))

    return lReturn
