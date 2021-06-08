
from vsg import parser

from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_tokens_at_beginning_of_line_matching_unless_between_tokens(lTokens, lUnless, lAllTokens, oTokenMap):

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lIndexes = filter_indexes_in_unless_regions(lIndexes, lUnless, oTokenMap)

    lReturn = []
    for iIndex in lIndexes:
        if oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 1):
            iLine = oTokenMap.get_line_number_of_index(iIndex)
            lReturn.append(tokens.New(iIndex, iLine, [lAllTokens[iIndex]]))
        elif oTokenMap.is_token_at_index(parser.carriage_return, iIndex - 2) and oTokenMap.is_token_at_index(parser.whitespace, iIndex - 1):
            iLine = oTokenMap.get_line_number_of_index(iIndex)
            lReturn.append(tokens.New(iIndex - 1, iLine, lAllTokens[iIndex - 1: iIndex + 1]))


    return lReturn


def filter_indexes_in_unless_regions(lIndexes, lUnless, oTokenMap):
    lReturn = []

    lUnlessIndexes = utils.get_indexes_of_token_pairs(lUnless, oTokenMap)
    if len(lUnlessIndexes) == 0:
        return lIndexes

    for iIndex in lIndexes:
        bAppend = True
        for unless in lUnlessIndexes:
            if iIndex >= unless[0] and iIndex <= unless[1]:
                bAppend = False
                break
        if bAppend:
            lReturn.append(iIndex)

    return lReturn
