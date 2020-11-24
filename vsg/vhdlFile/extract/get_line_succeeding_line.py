
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_line_succeeding_line(iLine, lAllTokens, iNumLines=1):

    iMyLine = 0
    iTargetLine = iLine + 1
    iEndLine = iLine + iNumLines + 1
    bStoreTokens = False
    lTemp = []
    iCount = 0
    for iToken, oToken in enumerate(lAllTokens):
        if bStoreTokens:
            lTemp.append(oToken)
        if isinstance(oToken, parser.carriage_return):
            iMyLine += 1
            if iMyLine == iTargetLine:
                bStoreTokens = True
                iStartIndex = iToken + 1
            if iMyLine == iEndLine:
                lTemp.pop()
                return utils.Tokens(iStartIndex, iTargetLine, lTemp)

    return None
