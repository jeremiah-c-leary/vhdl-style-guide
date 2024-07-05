# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.vhdlFile.extract import utils


def get_blank_lines_above_line_starting_with_use_clause(lTokens, lAllTokens, oTokenMap):
    lIndexes = get_list_of_indexes(lTokens, oTokenMap)
    lToi = utils.get_all_blank_lines_above_indexes(lIndexes, lAllTokens, oTokenMap)
    lToi = filter_design_unit(lToi, oTokenMap)
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
        oToi.set_meta_data("previous_library", None)
    else:
        oToken = lAllTokens[lTokenIndex[0]]
        oToi.set_meta_data("previous_library", oToken.get_lower_value())


def update_current_library(oToi, lAllTokens, oTokenMap):
    iLineNumber = oToi.get_line_number()
    iStartIndex = oTokenMap.get_index_of_line(iLineNumber)
    iLineNumber += 1
    iEndIndex = oTokenMap.get_index_of_line(iLineNumber)
    lTokenIndex = oTokenMap.get_token_indexes_between_indexes(token.use_clause.library_name, iStartIndex, iEndIndex)
    oToken = lAllTokens[lTokenIndex[0]]
    oToi.set_meta_data("current_library", oToken.get_lower_value())


def get_list_of_indexes(lTokens, oTokenMap):
    lIndexes = utils.get_indexes_of_token_list(lTokens, oTokenMap)
    lIndexes = utils.filter_indexes_which_start_a_line(lIndexes, oTokenMap)
    return lIndexes


def filter_design_unit(lToi, oTokenMap):
    lReturn = filter_context_clause(lToi, oTokenMap)
    lReturn = filter_library_unit(lReturn, oTokenMap)
    return lReturn


def filter_context_clause(lToi, oTokenMap):
    return filter_context_reference(lToi, oTokenMap)


def filter_library_unit(lToi, oTokenMap):
    lReturn = filter_primary_unit(lToi, oTokenMap)
    lReturn = filter_secondary_unit(lReturn, oTokenMap)
    return lReturn


def filter_primary_unit(lToi, oTokenMap):
    lReturn = filter_entity_declaration(lToi, oTokenMap)
    lReturn = filter_configuration_declaration(lReturn, oTokenMap)
    lReturn = filter_package_declaration(lReturn, oTokenMap)
    lReturn = filter_package_instantiation_declaration(lReturn, oTokenMap)
    lReturn = filter_context_declaration(lReturn, oTokenMap)
    return lReturn


def filter_secondary_unit(lToi, oTokenMap):
    lReturn = filter_architecture_body(lToi, oTokenMap)
    lReturn = filter_package_body(lReturn, oTokenMap)
    return lReturn


def filter_architecture_body(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.architecture_body.semicolon)


def filter_package_body(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.package_body.semicolon)


def filter_entity_declaration(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.entity_declaration.semicolon)


def filter_configuration_declaration(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.configuration_declaration.semicolon)


def filter_package_declaration(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.package_declaration.semicolon)


def filter_package_instantiation_declaration(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.package_instantiation_declaration.semicolon)


def filter_context_declaration(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.context_declaration.semicolon)


def filter_context_reference(lToi, oTokenMap):
    return filter_based_on_token(lToi, oTokenMap, token.context_reference.semicolon)


def filter_based_on_token(lToi, oTokenMap, oToken):
    lReturn = []
    for oToi in lToi:
        iIndex = oToi.iStartIndex
        if not oTokenMap.is_previous_non_whitespace_token(iIndex, oToken):
            lReturn.append(oToi)
    return lReturn
