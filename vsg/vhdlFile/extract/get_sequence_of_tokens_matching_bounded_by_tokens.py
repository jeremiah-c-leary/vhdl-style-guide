
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_sequence_of_tokens_matching_bounded_by_tokens(lTokens, oStart, oEnd, lAllTokens):
    iLine = 1
    lTemp = []
    lReturn = []
    iMatchCount = 0
    iMatchLength = len(lTokens)
    iStart = 0
    bCheck = False
    for iIndex in range(0, len(lAllTokens)):

        if isinstance(lAllTokens[iIndex], oStart):
            bCheck = True
            lTemp = []
            iMatchCount = 0
        if isinstance(lAllTokens[iIndex], oEnd):
            bCheck = False
            lTemp = []
            iMatchCount = 0

        if bCheck:
            if isinstance(lAllTokens[iIndex], lTokens[iMatchCount]):
                if iMatchCount == 0:
                    iStart = iIndex
                lTemp.append(lAllTokens[iIndex])
                iMatchCount +=1
                if iMatchCount == iMatchLength:
                    lReturn.append(utils.Tokens(iStart, iLine, lTemp))
                    lTemp = []
                    iMatchCount = 0
            elif iMatchCount > 0:
                lTemp = []
                iMatchCount = 0

        if isinstance(lAllTokens[iIndex], parser.carriage_return):
            iLine +=1

    return lReturn
