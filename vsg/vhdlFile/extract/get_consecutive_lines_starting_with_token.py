
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_consecutive_lines_starting_with_token(search_token, min_num_lines, lAllTokens, oTokenMap):

    lReturn = []
    lSearchIndexes = utils.filter_indexes_which_start_a_line(search_token, oTokenMap)

    lSearchLines = []
    for iSearchIndex in lSearchIndexes:
        lSearchLines.append(oTokenMap.get_line_number_of_index(iSearchIndex))

    iStart = None
    for iIndex, iLine in enumerate(lSearchLines):

        if iStart is None:
            iStart = iLine
            iStartLine = iLine
            iStartIndex = iIndex
            iCurrent = iLine
        else:
            if iLine == iCurrent + 1:
                iCurrent = iLine
                iEndIndex = iIndex
            else:
                if lSearchLines[iIndex - 1] - iStartLine >= min_num_lines - 1:
                    iStartToken = oTokenMap.get_index_of_carriage_return_before_index(lSearchIndexes[iStartIndex]) + 1
                    iEndToken = oTokenMap.get_index_of_carriage_return_after_index(lSearchIndexes[iEndIndex])
                    lTemp = lAllTokens[iStartToken:iEndToken]
                    lReturn.append(tokens.New(iStartToken, iStartLine, lTemp))
                iStart = iLine
                iStartLine = iLine
                iStartIndex = iIndex
                iCurrent = iLine

    if lSearchLines[iIndex - 1] - iStartLine >= min_num_lines - 1:
        iStartToken = oTokenMap.get_index_of_carriage_return_before_index(lSearchIndexes[iStartIndex]) + 1
        iEndToken = oTokenMap.get_index_of_carriage_return_after_index(lSearchIndexes[iEndIndex])
        lTemp = lAllTokens[iStartToken:iEndToken]
        lReturn.append(tokens.New(iStartToken, iStartLine, lTemp))

    return lReturn
