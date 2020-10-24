
from vsg import parser

from vsg.vhdlFile import vhdlFile as token_class

from vsg.vhdlFile import utils

def get_n_token_after_tokens(iToken, lTokens, lAllTokens):
    iLine = 1
    lReturn = []
    bSearch = False
    for iIndex in range(0, len(lAllTokens)):
        for oToken in lTokens:
            if isinstance(lAllTokens[iIndex], oToken):
                lReturn.append(search_for_next_n_token(iToken, iLine, iIndex + 1, lAllTokens))

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn


def search_for_next_n_token(iN, iLine, iToken, lAllTokens):
    iSearchLine = iLine
    iNTokens = 0
    for iSearch in range(iToken, len(lAllTokens)):
        oToken = lAllTokens[iSearch]
        if isinstance(oToken, parser.carriage_return):
            iSearchLine += 1
        if not isinstance(oToken, parser.whitespace) and \
           not isinstance(oToken, parser.carriage_return) and \
           not isinstance(oToken, parser.comment):
            iNTokens += 1
            if iNTokens == iN:
                return token_class.Tokens(iSearch, iSearchLine, [oToken])
