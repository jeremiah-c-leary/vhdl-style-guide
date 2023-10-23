
from vsg import parser
from vsg import token

from vsg.vhdlFile.extract import utils


def get_blank_lines_above_line_starting_with_use_clause(lTokens, lAllTokens, oTokenMap):

    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lIndexes = utils.filter_indexes_which_start_a_line(lIndexes, oTokenMap)
    lToi = utils.get_all_blank_lines_above_indexes(lIndexes, lAllTokens, oTokenMap)
    for oToi in lToi:
        update_previous_library(oToi, lAllTokens, oTokenMap) 
        update_current_library(oToi, lAllTokens, oTokenMap)
    return lToi


def update_previous_library(oToi, lAllTokens, oTokenMap):
        iEndIndex = oToi.get_start_index()
        iLineNumber = oTokenMap.get_line_number_of_index(iEndIndex)
        iStartIndex = oTokenMap.get_index_of_line(iLineNumber)
        lTokenIndex = oTokenMap.get_token_indexes_between_indexes(token.use_clause.library_name, iStartIndex, iEndIndex)
        if len(lTokenIndex) == 0:
            oToi.set_meta_data('previous_library', None)
        else:
            oToken = lAllTokens[lTokenIndex[0]]
            oToi.set_meta_data('previous_library', oToken.get_value().lower())

def update_current_library(oToi, lAllTokens, oTokenMap):
        iLineNumber = oToi.get_line_number()
        iStartIndex = oTokenMap.get_index_of_line(iLineNumber)
        iLineNumber =+ 1
        iEndIndex = oTokenMap.get_index_of_line(iLineNumber)
        lTokenIndex = oTokenMap.get_token_indexes_between_indexes(token.use_clause.library_name, iStartIndex, iEndIndex)
        oToken = lAllTokens[lTokenIndex[0]]
        oToi.set_meta_data('current_library', oToken.get_value().lower())

