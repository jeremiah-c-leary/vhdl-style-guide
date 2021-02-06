

from vsg.vhdlFile.extract import utils

from vsg.vhdlFile.extract.get_line_succeeding_line import get_line_succeeding_line


def get_line_below_line_ending_with_several_possible_tokens(lTokens, lAllTokens, oTokenMap):

    lReturn = []

    lTokenIndexes = utils.get_indexes_of_tokens_between(lTokens[0], lTokens[1:], oTokenMap)

    lIndexes = []
    for iIndex in lTokenIndexes:
        if utils.is_token_at_end_of_line(iIndex, oTokenMap):
            lIndexes.append(iIndex)

    lLine = utils.get_line_numbers_of_indexes_in_list(lIndexes, oTokenMap)
    for iLine in lLine:
        oToi = get_line_succeeding_line(iLine, lAllTokens, 1, oTokenMap)
        if oToi is not None:
            lReturn.append(oToi)

    return lReturn
