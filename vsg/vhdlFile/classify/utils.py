# -*- coding: utf-8 -*-

from vsg import parser
from vsg.token import exponent, direction
from vsg.vhdlFile import utils


def classify_selected_name(oDataStructure, token):
    oDataStructure.advance_to_next_token()
    lTokens = oDataStructure.get_current_token_value().split(".")
    if oDataStructure.get_next_token_value().startswith('"'):
        lTokens[-1] = oDataStructure.get_next_token_value()
        oDataStructure.remove_token_at_offset(1)
    lNewTokens = build_selected_name_token_list(lTokens, token)
    oDataStructure.replace_current_token_with_list_of_tokens(lNewTokens)


def detect_production(oDataStructure, production):
    while oDataStructure.advance_to_next_token():
        if not production.detect(oDataStructure):
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


def assign_special_tokens(oDataStructure, oType):
    sValue = oDataStructure.get_current_token_lower_value()
    if sValue == ")":
        oDataStructure.replace_current_token_with(parser.close_parenthesis)
    elif sValue == "(":
        oDataStructure.replace_current_token_with(parser.open_parenthesis)
    elif sValue == "-":
        if isinstance(oDataStructure.lAllObjects[oDataStructure.iCurrent - 1], exponent.e_keyword):
            oDataStructure.replace_current_token_with(exponent.minus_sign)
        else:
            oDataStructure.replace_current_token_with(parser.todo)
    elif sValue == "+":
        if isinstance(lObjects[iCurrent - 1], exponent.e_keyword):
            oDataStructure.replace_current_token_with(exponent.plus_sign)
        else:
            oDataStructure.replace_current_token_with(parser.todo)
    elif sValue == "*":
        oDataStructure.replace_current_token_with(parser.todo)
    elif sValue == "**":
        oDataStructure.replace_current_token_with(parser.todo)
    elif sValue == "/":
        oDataStructure.replace_current_token_with(parser.todo)
    elif sValue == "downto":
        oDataStructure.replace_current_token_with(direction.downto)
    elif sValue == "to":
        oDataStructure.replace_current_token_with(direction.to)
    elif sValue == "others":
        oDataStructure.replace_current_token_with(choice.others_keyword)
    elif sValue == "=>":
        oDataStructure.replace_current_token_with(element_association.assignment)
    elif sValue == "e":
        if lObjects[iCurrent + 1].get_value().isdigit() or lObjects[iCurrent + 1].get_value() == "-" or lObjects[iCurrent + 1].get_value() == "+":
            oDataStructure.replace_current_token_with(exponent.e_keyword)
        else:
            oDataStructure.replace_current_token_with(oType)
    elif sValue == "=":
        oDataStructure.replace_current_token_with(relational_operator.equal)
    elif sValue == "/=":
        oDataStructure.replace_current_token_with(relational_operator.not_equal)
    elif sValue == "<":
        oDataStructure.replace_current_token_with(relational_operator.less_than)
    elif sValue == "<=":
        oDataStructure.replace_current_token_with(relational_operator.less_than_or_equal)
    elif sValue == ">":
        oDataStructure.replace_current_token_with(relational_operator.greater_than)
    elif sValue == ">=":
        oDataStructure.replace_current_token_with(relational_operator.greater_than_or_equal)
    elif sValue == "?=":
        oDataStructure.replace_current_token_with(relational_operator.question_equal)
    elif sValue == "?/=":
        oDataStructure.replace_current_token_with(relational_operator.question_not_equal)
    elif sValue == "?<":
        oDataStructure.replace_current_token_with(relational_operator.question_less_than)
    elif sValue == "?<=":
        oDataStructure.replace_current_token_with(relational_operator.question_less_than_or_equal)
    elif sValue == "?>":
        oDataStructure.replace_current_token_with(relational_operator.question_greater_than)
    elif sValue == "?>=":
        oDataStructure.replace_current_token_with(relational_operator.question_greater_than_or_equal)

    elif exponent_detected(oDataStructure):
        oDataStructure.replace_current_token_with(exponent.integer)
    else:
        oDataStructure.replace_current_token_with(oType)


def exponent_detected(oDataStructure):
    iPreviousIndex = oDataStructure.get_current_index() - 1
    oToken = oDataStructure.lAllObjects[oDataStructure.get_current_index() - 1]
    if isinstance(oToken, exponent.e_keyword):
        return True
    if isinstance(oToken, exponent.plus_sign):
        return True
    if isinstance(oToken, exponent.minus_sign):
        return True
    return False


def is_current_token_open_paren(oDataStructure):
    return oDataStructure.current_token_lower_value_is("(")


def is_current_token_close_paren(oDataStructure):
    return oDataStructure.current_token_lower_value_is(")")


def unmatched_close_paren_found(iParen):
    return iParen == -1
