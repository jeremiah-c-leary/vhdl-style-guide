# -*- coding: utf-8 -*-

from vsg import parser, utils


def get_column_of_token_index(iToken, indent_size, lAllTokens, oTokenMap):
    oToken = lAllTokens[iToken]
    iLine = oTokenMap.get_line_number_of_index(iToken) - 1
    lCarriageReturns = oTokenMap.get_token_indexes(parser.carriage_return)
    iStart = lCarriageReturns[iLine - 1] + 1

    iReturn = 0
    for oToken in lAllTokens[iStart:iToken]:
        iReturn += len(utils.convert_tabs_to_spaces(oToken.get_value(), indent_size))
    return iReturn
