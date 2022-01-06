
from vsg.vhdlFile.extract import utils


def get_blank_lines_above_line_starting_with_token_when_between_tokens(lTokens, lBetweenTokens, lAllTokens, oTokenMap):

    lIndexes = utils.filter_tokens_between_tokens(lTokens, lBetweenTokens[0], lBetweenTokens[1], oTokenMap)
    lIndexes = utils.filter_indexes_which_start_a_line(lIndexes, oTokenMap)
    return utils.get_all_blank_lines_above_indexes(lIndexes, lAllTokens, oTokenMap)
