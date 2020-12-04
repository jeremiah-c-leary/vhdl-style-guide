
from vsg.vhdlFile.extract import utils

from vsg.vhdlFile.extract.get_line_succeeding_line import get_line_succeeding_line


def get_line_below_line_ending_with_token_with_hierarchy(lTokens, lAllTokens, lHierarchy, oTokenMap):

    lReturn = []

    lTokenIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    lIndexes = []
    for iIndex in lTokenIndexes:
        if lAllTokens[iIndex].get_hierarchy() in lHierarchy:
            if utils.is_token_at_end_of_line(iIndex, oTokenMap):
                lIndexes.append(iIndex)

    lLine = utils.get_line_numbers_of_indexes_in_list(lIndexes, oTokenMap)

    for iLine in lLine:
        lReturn.append(get_line_succeeding_line(iLine, lAllTokens, 1, oTokenMap))

    return lReturn
