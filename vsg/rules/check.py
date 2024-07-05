# -*- coding: utf-8 -*-

from vsg.rules import create_violation, utils as rules_utils


def add_new_line_and_remove_new_line(self, oToi, sOption, oTokenType):
    if sOption == "ignore":
        return
    elif sOption == "add_new_line":
        rules_utils.analyze_with_function(self, oToi, oTokenType, analyze_add_new_line_before)
    elif sOption == "remove_new_line":
        rules_utils.analyze_with_function(self, oToi, oTokenType, analyze_remove_new_line_before)


def analyze_add_new_line_before(self, oToi):
    iToken = oToi.get_meta_data("iToken")
    lTokens = oToi.get_tokens()
    if not rules_utils.token_at_beginning_of_line_in_token_list(iToken, lTokens):
        oViolation = create_violation.add_new_line(oToi)
        self.add_violation(oViolation)


def analyze_remove_new_line_before(self, oToi):
    iToken = oToi.get_meta_data("iToken")
    lTokens = oToi.get_tokens()
    if rules_utils.token_at_beginning_of_line_in_token_list(iToken, lTokens):
        oViolation = create_violation.remove_new_line(self, oToi)
        self.add_violation(oViolation)


def add_new_line_and_remove_new_line_after(self, oToi, sOption, oTokenType):
    if sOption == "ignore":
        return
    elif sOption == "add_new_line":
        rules_utils.analyze_with_function(self, oToi, oTokenType, analyze_add_new_line_after)
    elif sOption == "remove_new_line":
        rules_utils.analyze_with_function(self, oToi, oTokenType, analyze_remove_new_line_after)


def analyze_add_new_line_after(self, oToi):
    iToken = oToi.get_meta_data("iToken")
    lTokens = oToi.get_tokens()
    if not rules_utils.token_is_at_end_of_line(iToken, lTokens):
        oViolation = create_violation.add_new_line_after(oToi)
        self.add_violation(oViolation)


def analyze_remove_new_line_after(self, oToi):
    iToken = oToi.get_meta_data("iToken")
    lTokens = oToi.get_tokens()
    if rules_utils.token_is_at_end_of_line(iToken, lTokens):
        oViolation = create_violation.remove_new_line_after(self, oToi)
        self.add_violation(oViolation)
