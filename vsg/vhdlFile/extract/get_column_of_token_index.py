
from vsg import parser


def get_column_of_token_index(iToken, lAllTokens):
    iReturn = 0
    for iIndex in range(iToken - 1, 0, -1):
        oToken = lAllTokens[iIndex]
        if isinstance(oToken, parser.carriage_return):
            return iReturn
        iReturn += len(lAllTokens[iIndex].get_value())
    return iReturn
