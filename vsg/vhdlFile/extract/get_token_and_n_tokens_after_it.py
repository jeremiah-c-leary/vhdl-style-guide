
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_token_and_n_tokens_after_it(lTokens, iTokens, lAllTokens, oTokenMap):
    lReturn = []

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iEnd = iIndex + iTokens + 1
        lReturn.append(tokens.New(iIndex, iLine, lAllTokens[iIndex:iEnd]))

    return lReturn
