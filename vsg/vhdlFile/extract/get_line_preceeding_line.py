
from vsg import parser

from vsg.vhdlFile import vhdlFile as utils


def get_line_preceeding_line(iLine, lAllTokens):

    iMyLine = 1
    iTargetLine = iLine - 1
    bStoreTokens = False
    lTemp = []
    for iToken, oToken in enumerate(lAllTokens):
        if bStoreTokens:
            lTemp.append(oToken)
        if isinstance(oToken, parser.carriage_return):
            iMyLine += 1
            if bStoreTokens:
                lTemp.pop()
                return utils.Tokens(iStartIndex, iTargetLine, lTemp)
            if iMyLine == iTargetLine:
                bStoreTokens = True
                iStartIndex = iToken + 1

    return None
