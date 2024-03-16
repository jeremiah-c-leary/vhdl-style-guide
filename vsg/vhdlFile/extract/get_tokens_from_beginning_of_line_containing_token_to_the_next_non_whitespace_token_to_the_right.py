# -*- coding: utf-8 -*-

from vsg.vhdlFile.extract import tokens


def get_tokens_from_beginning_of_line_containing_token_to_the_next_non_whitespace_token_to_the_right(token, lAllTokens, oTokenMap):
    lReturn = []

    lToken = oTokenMap.get_token_indexes(token)

    for iToken in lToken:
        iLine = oTokenMap.get_line_number_of_index(iToken)
        iStart = oTokenMap.get_index_of_carriage_return_before_index(iToken)
        iEnd = oTokenMap.get_index_of_next_non_whitespace_token_after_index_ignoring_comments(iToken)

        oTokens = tokens.New(iStart, iLine, lAllTokens[iStart : iEnd + 1])
        oTokens.set_meta_data("iTokenIndex", iToken - iStart)
        lReturn.append(oTokens)

    return lReturn
