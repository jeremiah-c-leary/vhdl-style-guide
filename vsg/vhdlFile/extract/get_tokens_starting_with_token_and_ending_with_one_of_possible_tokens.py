
from vsg.vhdlFile.extract import utils

from vsg.vhdlFile.extract import tokens

from vsg.vhdlFile import utils as vhdl_utils


def get_tokens_starting_with_token_and_ending_with_one_of_possible_tokens(lStartTokens, lEndTokens, lAllTokens, oTokenMap, bIncludeStartToken=False, bIncludeEndToken=True, bEarliestDetect=False):
    '''
    Returns a list of tokens objects which start with a token and ends

    This extract function is intended for situations in which the start of a sequence of tokens is known, but the end token can vary due to optional language constructs.

    Parameters:

      lStartTokens : list of token types

      lEndTokens : list of token types

      lAllTokens : list of token objects

      oTokenMap : token map object

      bIncludeStartToken : boolean
          True  = Include the starting bounding token from lStartTokens
          False = Exclude the starting bounding token from lStartTokens and leading whitesapce and comments

      bIncludeEndToken : boolean
          True  = Include the ending bounding token from lEndTokens
          False = Exclude the ending bounding token from lEndTokens and trailing whitespace and comments

      bEarliestDetect : boolean
          True  = the first token in the lEndTokens bounds the list of tokens
          False = the last token in the lEndTokens bounds the list of tokens
    '''
    lReturn = []

    lStartIndexes = gather_start_indexes(lStartTokens, oTokenMap, bIncludeStartToken)

    lEndIndexes, iMax = gather_end_indexes(lEndTokens, oTokenMap)

    lStartIndexes.append(iMax)

    iStart, iEnd, iStep = set_loop_parameters(bEarliestDetect, lEndTokens)

    for iIndex, iStartIndex in enumerate(lStartIndexes[:len(lStartIndexes) - 1]):
        iNextIndex = lStartIndexes[iIndex + 1]
        for i in range(iStart, iEnd, iStep):
            lEndIndexTemp = lEndIndexes[i]
            bBreak = False
            for iEndTemp in lEndIndexTemp:
                if iStartIndex < iEndTemp and iEndTemp < iNextIndex:
                    iLine = oTokenMap.get_line_number_of_index(iStartIndex)
                    if bIncludeEndToken:
                        iStartIndex, lTemp = vhdl_utils.remove_leading_whitespace_and_comments(iStartIndex, lAllTokens[iStartIndex:iEndTemp + 1])
                    else:
                        iStartIndex, lTemp = vhdl_utils.remove_leading_whitespace_and_comments(iStartIndex, lAllTokens[iStartIndex:iEndTemp])
                    lNewTemp = vhdl_utils.remove_trailing_whitespace_and_comments(lTemp)
                    lReturn.append(tokens.New(iStartIndex - 1, iLine, lNewTemp))
                    bBreak = True
                    break
            if bBreak:
                break
    return lReturn


def gather_start_indexes(lStartTokens, oTokenMap, bIncludeStartToken):
    lStartIndexesTemp = utils.get_indexes_of_token_list(lStartTokens, oTokenMap)
    if bIncludeStartToken:
        lStartIndexes = lStartIndexesTemp
    else:
        lStartIndexes = []
        for iIndex in lStartIndexesTemp:
            lStartIndexes.append(iIndex + 1)

    return lStartIndexes


def gather_end_indexes(lEndTokens, oTokenMap):
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

    return lEndIndexes, iMax

def set_loop_parameters(bEarliestDetect, lEndTokens):
    if bEarliestDetect:
        iStart = 0
        iEnd = len(lEndTokens)
        iStep = 1
    else:
        iStart = len(lEndTokens) - 1
        iEnd = -1
        iStep = -1
    return iStart, iEnd, iStep
