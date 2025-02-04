# -*- coding: utf-8 -*-

from vsg.vhdlFile import utils


def classify_selected_name(oDataStructure, token):
    oDataStructure.advance_to_next_token()
    lTokens = oDataStructure.get_current_token_value().split(".")
    if oDataStructure.get_next_token_value().startswith('"'):
        lTokens[-1] = oDataStructure.get_next_token_value()
        oDataStructure.remove_token_at_offset(1)
    lNewTokens = build_selected_name_token_list(lTokens, token)
    oDataStructure.replace_current_token_with_list_of_tokens(lNewTokens)


def detect_production(oDesignFile, production):
    while oDesignFile.advance_to_next_token():
        if not production.detect(oDesignFile):
            return False
    return False


def build_selected_name_token_list(lTokens, token):
    if is_use_clause_selected_name(token):
        return build_use_clause_selected_name_token_list(lTokens, token)
    return build_context_reference_selected_name_token_list(lTokens, token)


def build_use_clause_selected_name_token_list(lTokens, token):
    lNewTokens = []
    for iThisToken, sToken in enumerate(lTokens):
        classify_use_clause_selected_name_elements(iThisToken, lNewTokens, lTokens, token)
    lNewTokens.pop()
    return lNewTokens


def build_context_reference_selected_name_token_list(lTokens, token):
    lNewTokens = []
    for iThisToken, sToken in enumerate(lTokens):
        classify_context_reference_selected_name_elements(iThisToken, lNewTokens, lTokens, token)
    lNewTokens.pop()
    return lNewTokens


def classify_use_clause_selected_name_elements(iThisToken, lNewTokens, lTokens, token):
    sToken = lTokens[iThisToken]
    if iThisToken == 0:
        lNewTokens.append(token.library_name(sToken))
    elif sToken.lower() == "all":
        lNewTokens.append(token.all_keyword(sToken))
    elif iThisToken == len(lTokens) - 1:
        lNewTokens.append(token.item_name(sToken))
    else:
        lNewTokens.append(token.package_name(sToken))
    lNewTokens.append(token.dot())


def classify_context_reference_selected_name_elements(iThisToken, lNewTokens, lTokens, token):
    sToken = lTokens[iThisToken]
    if iThisToken == 0 and len(lTokens) > 1:
        lNewTokens.append(token.library_name(sToken))
    else:
        lNewTokens.append(token.context_name(sToken))
    lNewTokens.append(token.dot())


def replace_item_in_list_with_a_list_at_index(lFirstList, lSecondList, iIndex):
    lFirstList.pop(iIndex)
    lSecondList.reverse()
    for oToken in lSecondList:
        lFirstList.insert(iIndex, oToken)


def is_use_clause_selected_name(token):
    if token.__name__ == "vsg.token.use_clause":
        return True
    return False


def classify_production(production, iToken, lObjects):
    iCurrent = iToken
    iStop = len(lObjects)
    while iCurrent < iStop:
        iPrevious = iCurrent
        iCurrent = production.detect(iCurrent, lObjects)
        if iPrevious == iCurrent:
            break
    return iCurrent
