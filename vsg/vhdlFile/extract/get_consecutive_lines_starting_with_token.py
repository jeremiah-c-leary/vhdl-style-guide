
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_consecutive_lines_starting_with_token(search_token, min_num_lines, lAllTokens, oTokenMap):

    lReturn = []
    lSearchLines = get_line_numbers_of_tokens_which_start_line(search_token, oTokenMap)
    lGroups = group_lines(lSearchLines)
    lFilteredGroups = filter_groups_based_on_number_of_lines(lGroups, min_num_lines)

    for lGroup in lFilteredGroups:
        iStartLine = lGroup[0]
        iEndLine = lGroup[-1]
        iStartToken = oTokenMap.get_index_of_line(iStartLine)
        iEndToken = oTokenMap.get_index_of_carriage_return_after_index(oTokenMap.get_index_of_line(iEndLine))
        lTemp = lAllTokens[iStartToken:iEndToken]

        lReturn.append(tokens.New(iStartToken, iStartLine, lTemp))

    return lReturn


def get_line_numbers_of_tokens_which_start_line(search_token, oTokenMap):
    lSearchIndexes = utils.filter_tokens_which_start_a_line(search_token, oTokenMap)
    lSearchLines = []
    for iSearchIndex in lSearchIndexes:
        lSearchLines.append(oTokenMap.get_line_number_of_index(iSearchIndex))
    return lSearchLines


def group_lines(lLines):
    lReturn = []
    if len(lLines) == 0:
        return []
    lTemp = [lLines[0]]
    for iLine in lLines[1:]:
        if iLine == lTemp[-1] + 1:
            lTemp.append(iLine)
        else:
            lReturn.append(lTemp)
            lTemp = [iLine]

    lReturn.append(lTemp)

    return lReturn


def filter_groups_based_on_number_of_lines(lGroups, min_num_lines):
    lReturn = []
    for lGroup in lGroups:
        if len(lGroup) >= min_num_lines:
            lReturn.append(lGroup)
    return lReturn
