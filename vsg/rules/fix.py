
from vsg.rules import utils as rules_utils

from vsg.vhdlFile import utils


def fix_violation(oViolation):
    dAction = oViolation.get_action()
    if dAction['action'] == 'add_new_line':
        add_new_line(oViolation)
    elif dAction['action'] == 'remove_new_line':
        remove_new_line(oViolation)
    elif dAction['action'] == 'add_new_line_and_remove_carraige_returns':
        add_new_line_and_remove_carraige_returns(oViolation)


def add_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    rules_utils.remove_leading_whitespace_tokens(lTokens)
    rules_utils.insert_whitespace(lTokens, 0)
    rules_utils.insert_carriage_return(lTokens, 0)
    oViolation.set_tokens(lTokens)


def remove_new_line(oViolation):
    lTokens = oViolation.get_tokens()
    lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
    utils.remove_consecutive_whitespace_tokens(lTokens)
    rules_utils.remove_leading_whitespace_tokens(lTokens)
    rules_utils.change_all_whitespace_to_single_character(lTokens)
    lNewTokens = utils.remove_trailing_whitespace(lTokens)
    utils.fix_blank_lines(lNewTokens)
    oViolation.set_tokens(lNewTokens)


def add_new_line_and_remove_carraige_returns(oViolation):
    lTokens = oViolation.get_tokens()
    lTokens = utils.remove_carriage_returns_from_token_list(lTokens)
    rules_utils.remove_leading_whitespace_tokens(lTokens)
    rules_utils.insert_whitespace(lTokens, 0)
    rules_utils.insert_carriage_return(lTokens, 0)
    rules_utils.change_all_whitespace_to_single_character(lTokens)
    utils.fix_blank_lines(lTokens)
    oViolation.set_tokens(lTokens)
