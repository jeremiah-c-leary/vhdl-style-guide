
from vsg import parser

from vsg.vhdlFile.extract import utils


def get_blank_lines_above_line_starting_with_token(lTokens, lAllTokens, oTokenMap):

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lIndexes = utils.filter_indexes_which_start_a_line(lIndexes, oTokenMap)
    return utils.get_all_blank_lines_above_indexes(lIndexes, lAllTokens, oTokenMap)
