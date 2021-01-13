
from vsg.vhdlFile.extract import utils

from vsg.vhdlFile.extract.get_line_preceeding_line import get_line_preceeding_line


def get_line_above_line_starting_with_token_with_hierarchy(lTokens, lAllTokens, lHierarchy, oTokenMap, bIncludeComments=False):

    lReturn = []

    lTokenIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    lIndexes = []
    for iIndex in lTokenIndexes:
        if lAllTokens[iIndex].get_hierarchy() in lHierarchy:
            if utils.is_token_at_start_of_line(iIndex, oTokenMap):
                lIndexes.append(iIndex)

    lLine = utils.get_line_numbers_of_indexes_in_list(lIndexes, oTokenMap)

    for iLine in lLine:
        lReturn.append(get_line_preceeding_line(iLine, lAllTokens, 1, oTokenMap, bIncludeComments))

    return lReturn
