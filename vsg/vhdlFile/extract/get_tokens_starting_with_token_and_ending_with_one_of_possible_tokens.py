
from vsg.vhdlFile.extract import utils

from vsg.vhdlFile.extract import tokens

from vsg.vhdlFile import utils as vhdl_utils


def get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(lStartTokens, lEndTokens, lAllTokens, oTokenMap):
    lReturn = []

    lStartIndexesTemp = utils.get_indexes_of_token_list(lStartTokens, oTokenMap)
    lStartIndexes = []
    for iIndex in lStartIndexesTemp:
        lStartIndexes.append(iIndex + 1)

    lEndIndexes = []
    iMax = 0
    iMaxLength = 0
    for oToken in lEndTokens:
        lIndexes = oTokenMap.get_token_indexes(oToken)
        lEndIndexes.append(lIndexes)
        try:
            iMax = max(iMax, lIndexes[-1])
        except IndexError:
            iMax = iMax
        iMaxLength = max(iMaxLength, len(lIndexes))
    iMax +=1
    lStartIndexes.append(iMax)

    iEndLength = len(lEndTokens)
    for iIndex, iStartIndex in enumerate(lStartIndexes[:len(lStartIndexes) - 1]):
        iNextIndex = lStartIndexes[iIndex + 1]
        for i in range(iEndLength - 1, -1, -1):
            lEndIndexTemp = lEndIndexes[i]
            bBreak = False
            for iEndTemp in lEndIndexTemp:
                if iStartIndex < iEndTemp and iEndTemp < iNextIndex:
                    iLine = oTokenMap.get_line_number_of_index(iStartIndex)
                    iStartIndex, lTemp = vhdl_utils.remove_leading_whitespace_and_comments(iStartIndex, lAllTokens[iStartIndex:iEndTemp + 1])
                    lReturn.append(tokens.New(iStartIndex - 1, iLine, lTemp))
                    bBreak = True
                    break
            if bBreak:
                break
    return lReturn
