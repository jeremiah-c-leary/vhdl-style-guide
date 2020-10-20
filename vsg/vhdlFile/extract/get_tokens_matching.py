
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_tokens_matching(lTokens, lAllTokens):
    iLine = 1
    lReturn = []
    for iIndex in range(0, len(lAllTokens)):
        for oToken in lTokens:
            if isinstance(lAllTokens[iIndex], oToken):
                lReturn.append(utils.Tokens(iIndex, iLine, [lAllTokens[iIndex]]))

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn
