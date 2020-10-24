
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_first_token_after_tokens(lTokens, lAllTokens):
    iLine = 1
    lReturn = []
    for iIndex in range(0, len(lAllTokens)):
        for oToken in lTokens:
            if isinstance(lAllTokens[iIndex], oToken):
                lReturn.append(search_for_next_token(iLine, iIndex + 1, lAllTokens))

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn


def search_for_next_token(iLine, iToken, lAllTokens):
    iSearchLine = iLine
    for iSearch in range(iToken, len(lAllTokens)):
        oToken = lAllTokens[iSearch]

        if isinstance(oToken, parser.carriage_return):
            iSearchLine += 1
        if not isinstance(oToken, parser.whitespace) and \
           not isinstance(oToken, parser.carriage_return) and \
           not isinstance(oToken, parser.comment):
            return utils.Tokens(iSearch, iSearchLine, [oToken])
