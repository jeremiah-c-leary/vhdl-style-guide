
from vsg.vhdlFile.extract import tokens
from vsg.vhdlFile.extract import utils


def get_m_tokens_before_and_n_tokens_after_token(iM, iN, lTokens, lAllTokens, oTokenMap):
    lReturn = []

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iStart = iIndex - iM
        iEnd = iIndex + iN
        if iStart >= 0:
            lReturn.append(tokens.New(iStart, iLine, lAllTokens[iStart:iEnd + 1]))

    return lReturn
