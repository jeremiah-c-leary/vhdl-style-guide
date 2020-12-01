
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_m_tokens_before_and_n_tokens_after_token(iM, iN, lTokens, lAllTokens, oTokenMap):
    lReturn = []

    lIndexes = get_indexes_of_token_list(lTokens, oTokenMap)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iStart = iIndex - iM
        iEnd = iIndex + iN
        if iStart >= 0:
            lReturn.append(utils.Tokens(iStart, iLine, lAllTokens[iStart:iEnd + 1]))

    return lReturn


def get_indexes_of_token_list(lTokens, oTokenMap):
    lReturn = []
    for oToken in lTokens:
        lReturn.extend(oTokenMap.get_token_indexes(oToken))

    lReturn.sort()

    return lReturn
