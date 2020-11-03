
from vsg import parser
from vsg.vhdlFile import vhdlFile as utils


def get_sequence_of_tokens_matching(lTokens, lAllTokens, bIgnoreIfLineStart=False):
    iLine = 1
    lTemp = []
    lReturn = []
    iMatchCount = 0
    iMatchLength = len(lTokens)
    iStart = 0
    for iIndex in range(0, len(lAllTokens)):

        if isinstance(lAllTokens[iIndex], lTokens[iMatchCount]):
            if iMatchCount == 0:
                iStart = iIndex
            lTemp.append(lAllTokens[iIndex])
            iMatchCount +=1
            if iMatchCount == iMatchLength:
                if bIgnoreIfLineStart and is_token_at_start_of_line(iStart, lAllTokens):
                    lTemp = []
                    iMatchCount = 0
                else:
                    lReturn.append(utils.Tokens(iStart, iLine, lTemp))
                    lTemp = []
                    iMatchCount = 0
        elif iMatchCount > 0:
            lTemp = []
            iMatchCount = 0

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn


def is_token_at_start_of_line(iToken, lAllTokens):
    if isinstance(lAllTokens[iToken - 1], parser.whitespace) and isinstance(lAllTokens[iToken - 2], parser.carriage_return):
        return True
    if isinstance(lAllTokens[iToken - 1], parser.carriage_return):
        return True
    return False
