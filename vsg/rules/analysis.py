# -*- coding: utf-8 -*-

from vsg import violation
from vsg.rules import utils as rules_utils
from vsg.vhdlFile import utils


def check_for_carriage_return_after_token(self, oToi):
    if self.value == "ignore":
        return []
    elif self.value == "no":
        return check_no(self, oToi)
    elif self.value == "yes":
        return check_yes(self, oToi)


def check_no(self, oToi):
    return check(self, oToi, "remove_new_line")


def check_yes(self, oToi):
    return check(self, oToi, "add_new_line")


def check(self, oToi, action):
    lTokens = oToi.get_tokens()
    iLine = oToi.get_line_number()
    lReturn = []

    value = set_check_value(action)

    for iToken, oToken in enumerate(lTokens):
        if rules_utils.token_exists_in_token_type_list(oToken, self.analysis_options):
            if utils.is_token_at_end_of_line(iToken, lTokens) == value:
                iViolation_line_number = iLine + rules_utils.number_of_carriage_returns(lTokens[0:iToken])
                sSolution = "jcl-fix this"
                iEndIndex = utils.find_next_non_whitespace_token(iToken + 1, lTokens) - 1
                oMyToi = oToi.extract_tokens(iToken + 1, iEndIndex)
                oViolation = violation.New(iViolation_line_number, oMyToi, sSolution)
                dAction = {}
                dAction["action"] = action
                oViolation.set_action(dAction)
                lReturn.append(oViolation)
    return lReturn


def set_check_value(action):
    if action == "remove_new_line":
        return True
    return False


def check_for_carriage_return_before_token(self, oToi):
    if self.value == "ignore":
        return []
    lTokens = oToi.get_tokens()
    iLine = oToi.get_line_number()
    lReturn = []

    for iToken, oToken in enumerate(lTokens):
        if rules_utils.token_exists_in_token_type_list(oToken, self.analysis_options):
            if rules_utils.token_at_beginning_of_line_in_token_list(iToken, lTokens) and self.value == "no":
                sSolution = "jcl-fix this"
                iViolation_line_number = iLine + rules_utils.number_of_carriage_returns(lTokens[0:iToken])
                iStartIndex = utils.find_previous_non_whitespace_token(iToken - 1, lTokens) + 1
                oMyToi = oToi.extract_tokens(iStartIndex, iToken - 1)
                oViolation = violation.New(iViolation_line_number, oMyToi, "jcl-fix this")
                dAction = {}
                dAction["action"] = "remove_new_line"
                oViolation.set_action(dAction)
                lReturn.append(oViolation)
            elif not rules_utils.token_at_beginning_of_line_in_token_list(iToken, lTokens) and self.value == "yes":
                sSolution = "jcl-fix this"
                iViolation_line_number = iLine + rules_utils.number_of_carriage_returns(lTokens[0:iToken])
                iStartIndex = utils.find_previous_non_whitespace_token(iToken - 1, lTokens) + 1
                oMyToi = oToi.extract_tokens(iStartIndex, iToken - 1)
                oViolation = violation.New(iViolation_line_number, oMyToi, "jcl-fix this")
                dAction = {}
                dAction["action"] = "add_new_line"
                oViolation.set_action(dAction)
                lReturn.append(oViolation)
    return lReturn


def check_for_carriage_returns_between_tokens_ignoring_leading_and_trailing_whitespace(self, oToi):
    if self.value == "ignore":
        return []
    lTokens = oToi.get_tokens()
    iLine = oToi.get_line_number()
    lReturn = []
    for lTokenPairs in self.analysis_options:
        for iToken, oToken in enumerate(lTokens):
            if isinstance(oToken, lTokenPairs[0]):
                iEndIndex = rules_utils.get_index_of_token_in_list(lTokenPairs[1], lTokens)
                if iEndIndex is None:
                    continue
                iStartIndex = utils.find_next_non_whitespace_token(iToken + 1, lTokens)
                iEndIndex = utils.find_previous_non_whitespace_token(iEndIndex - 1, lTokens)
                iNumberCarriageReturns = rules_utils.number_of_carriage_returns(lTokens[iStartIndex : iEndIndex + 1])
                if iNumberCarriageReturns > 0:
                    sSolution = "jcl-fix this"

                    iViolation_line_number = iLine + rules_utils.number_of_carriage_returns(lTokens[0:iStartIndex])
                    oMyToi = oToi.extract_tokens(iStartIndex, iEndIndex)
                    oViolation = violation.New(iViolation_line_number, oMyToi, "jcl-fix this")
                    dAction = {}
                    dAction["action"] = "remove_new_line"
                    oViolation.set_action(dAction)
                    lReturn.append(oViolation)
    return lReturn
