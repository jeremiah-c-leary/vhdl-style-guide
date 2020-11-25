
from vsg import parser

from vsg.vhdlFile import vhdlFile as token_class


def get_n_tokens_before_and_after_tokens(iToken, lTokens, lAllTokens):
    iLine = 1
    lReturn = []
    for iIndex in range(0, len(lAllTokens)):
        for oToken in lTokens:
            if isinstance(lAllTokens[iIndex], oToken):

                lReturn.append(token_class.Tokens(iIndex - iToken, iLine, lAllTokens[iIndex - iToken:iIndex + iToken + 1]))

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn
