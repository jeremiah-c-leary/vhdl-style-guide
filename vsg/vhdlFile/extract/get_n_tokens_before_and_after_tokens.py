
from vsg import parser

from vsg.vhdlFile import vhdlFile as token_class


def get_n_tokens_before_and_after_tokens(iToken, lTokens, lAllTokens, oTokenMap):
    lReturn = []
    lIndexes = []

    for oToken in lTokens:
        lIndexes.extend(oTokenMap.get_token_indexes(oToken))
    
    lIndexes.sort()
    
    for iIndex in lIndexes:
        iLine = oTokenMap.get_line_number_of_index(iIndex)
        lReturn.append(token_class.Tokens(iIndex - iToken, iLine, lAllTokens[iIndex - iToken:iIndex + iToken + 1]))
    
    return lReturn
