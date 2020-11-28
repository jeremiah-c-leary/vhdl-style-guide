
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_tokens_matching(lTokens, lAllTokens, oTokenMap):

    lReturn = []
    lIndexes = []

    for oToken in lTokens:
        lIndexes.extend(oTokenMap.get_token_indexes(oToken))
    
    lIndexes.sort()
    
    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lReturn.append(utils.Tokens(iIndex, iLine, [lAllTokens[iIndex]]))
    
    return lReturn
