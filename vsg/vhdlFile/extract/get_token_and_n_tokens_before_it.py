
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_token_and_n_tokens_before_it(lTokens, iTokens, lAllTokens, oTokenMap):
    lReturn = []

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iStart = iIndex - iTokens
        if iStart >= 0:
            lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart:iIndex + 1]))
    return lReturn
