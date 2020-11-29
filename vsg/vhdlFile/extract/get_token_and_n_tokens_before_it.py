
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_token_and_n_tokens_before_it(oToken, iTokens, lTokens, oTokenMap):

    lReturn = []
    lIndexes = []

    lIndexes = oTokenMap.get_token_indexes(oToken)

    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        iStart = iIndex - iTokens
        if iStart >= 0:
            lReturn.append(utils.Tokens(iStart, iLine, lTokens[iIndex - iTokens:iIndex + 1]))

    return lReturn
