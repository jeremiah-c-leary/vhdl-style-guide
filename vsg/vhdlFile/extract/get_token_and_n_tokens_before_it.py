
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_token_and_n_tokens_before_it(oToken, iTokens, lTokens):
    iLine = 1
    lReturn = []
    iStart = 0
    for iIndex in range(0, len(lTokens)):
        if isinstance(lTokens[iIndex], oToken):
            iStart = iIndex - iTokens
            if iStart >= 0:
                lReturn.append(utils.Tokens(iStart, iLine, lTokens[iIndex - iTokens:iIndex + 1]))

        if isinstance(lTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn
