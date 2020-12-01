
from vsg import parser

def get_column_of_token_index(iToken, lAllTokens, oTokenMap):

    oToken = lAllTokens[iToken]
    iLine = oTokenMap.get_line_number_of_index(iToken) - 1
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)
    iStart = lCarriageReturns[iLine - 1] + 1

    iReturn = 0
    for oToken in lAllTokens[iStart:iToken]:
        iReturn += len(oToken.get_value())
    return iReturn
