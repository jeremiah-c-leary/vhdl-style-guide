# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import blank_line
from vsg.rules.utils import token_is_comment, token_is_whitespace


class previous_line(blank_line.Rule):
    """
    Checks for a blank line above a line starting with a given token

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    token: token object type list
       token object that a blank line above should appear
    """

    def __init__(self, lTokens, lAllowTokens=None):
        super().__init__()
        self.solution = "Insert blank line above"
        self.lTokens = lTokens
        self.lHierarchyLimits = None
        self.style = "require_blank_line"
        self.configuration.append("style")
        if lAllowTokens is None:
            self.lAllowTokens = []
        else:
            self.lAllowTokens = lAllowTokens
        self.configuration_documentation_link = "configuring_previous_line_rules_link"

    def _get_tokens_of_interest(self, oFile):
        bIncludeComments = _include_comments(self.style)

        if self.style == "require_comment":
            if self.lHierarchyLimits is None:
                lFirst = oFile.get_line_above_line_starting_with_token(self.lTokens, False)
                lSecond = oFile.get_line_above_line_starting_with_token(self.lTokens, True)
                return zip(lFirst, lSecond)
            else:
                lFirst = oFile.get_line_above_line_starting_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits, False)
                lSecond = oFile.get_line_above_line_starting_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits, True)
                return zip(lFirst, lSecond)

        elif self.style == "no_blank_line":
            return oFile.get_blank_lines_above_line_starting_with_token(self.lTokens)
        elif self.style == "no_blank_line_unless_different_library":
            return oFile.get_blank_lines_above_line_starting_with_use_clause(self.lTokens)
        else:
            if self.lHierarchyLimits is None:
                return oFile.get_line_above_line_starting_with_token(self.lTokens, bIncludeComments)
            else:
                return oFile.get_line_above_line_starting_with_token_with_hierarchy(self.lTokens, self.lHierarchyLimits, bIncludeComments)

    def _set_allow_tokens(self):
        return

    def _analyze(self, lToi):
        self._set_allow_tokens()
        if self.style == "no_blank_line":
            _analyze_no_blank_line(self, lToi, self.lAllowTokens)
        elif self.style == "no_blank_line_unless_different_library":
            _analyze_no_blank_line_unless_different_library(self, lToi, self.lAllowTokens)
        elif self.style == "require_blank_line":
            _analyze_require_blank_line(self, lToi, self.lAllowTokens)
        elif self.style == "no_code":
            _analyze_no_code(self, lToi, self.lAllowTokens)
        elif self.style == "allow_comment":
            _analyze_no_code(self, lToi, self.lAllowTokens)
        elif self.style == "require_comment":
            _analyze_require_comment(self, lToi, self.lAllowTokens)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction["action"] == "Insert":
            lTokens.append(parser.carriage_return())
            lTokens.append(parser.blank_line())
            oViolation.set_tokens(lTokens)
        elif dAction["action"] == "Remove":
            oViolation.set_tokens([])


def _include_comments(sMethod):
    if sMethod == "require_blank_line":
        return False
    elif sMethod == "no_code":
        return False
    elif sMethod == "allow_comment":
        return True
    elif sMethod == "require_comment":
        return True
    return None


def _analyze_no_blank_line(self, lToi, lAllowTokens):
    for oToi in lToi:
        sSolution = "Remove blank lines"
        oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
        dAction = {}
        dAction["action"] = "Remove"
        oViolation.set_action(dAction)
        self.add_violation(oViolation)


def _analyze_no_blank_line_unless_different_library(self, lToi, lAllowTokens):
    for oToi in lToi:
        if oToi.get_meta_data("previous_library") == oToi.get_meta_data("current_library"):
            sSolution = "Remove blank lines"
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            dAction = {}
            dAction["action"] = "Remove"
            oViolation.set_action(dAction)
            self.add_violation(oViolation)
        elif oToi.get_meta_data("previous_library") is None:
            sSolution = "Remove blank lines"
            oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
            dAction = {}
            dAction["action"] = "Remove"
            oViolation.set_action(dAction)
            self.add_violation(oViolation)


def _analyze_require_blank_line(self, lToi, lAllowTokens):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if _is_allowed_token(lAllowTokens, lTokens):
            continue
        if len(lTokens) == 1:
            if isinstance(lTokens[0], parser.blank_line):
                continue
        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
        dAction = {}
        dAction["action"] = "Insert"
        oViolation.set_action(dAction)
        self.add_violation(oViolation)


def _analyze_no_code(self, lToi, lAllowTokens):
    for oToi in lToi:
        lTokens = oToi.get_tokens()
        if _is_allowed_token(lAllowTokens, lTokens):
            continue
        if len(lTokens) == 1:
            if isinstance(lTokens[0], parser.blank_line) or token_is_comment(lTokens[0]):
                continue
        elif len(lTokens) == 2:
            if token_is_whitespace(lTokens[0]) and token_is_comment(lTokens[1]):
                continue
        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
        dAction = {}
        dAction["action"] = "Insert"
        oViolation.set_action(dAction)
        self.add_violation(oViolation)


def _analyze_require_comment(self, lToi, lAllowTokens):
    for oFirstToi, oToi in list(lToi):
        lTokens = oFirstToi.get_tokens()
        if _is_allowed_token(lAllowTokens, lTokens):
            continue
        # Check if first line is a comment
        if not _comment_starts_line(lTokens):
            sSolution = "Comment required above this line."
            oViolation = violation.New(oFirstToi.get_line_number(), oFirstToi, sSolution)
            dAction = {}
            dAction["action"] = "Skip"
            oViolation.set_action(dAction)
            self.add_violation(oViolation)
            continue

        lTokens = oToi.get_tokens()
        if _is_allowed_token(lAllowTokens, lTokens):
            continue
        if len(lTokens) == 1:
            if isinstance(lTokens[0], parser.blank_line):
                continue
        elif len(lTokens) == 2:
            if token_is_whitespace(lTokens[0]) and token_is_comment(lTokens[1]) and self.allow_comment:
                continue
        oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
        dAction = {}
        dAction["action"] = "Insert"
        oViolation.set_action(dAction)
        self.add_violation(oViolation)


def _is_allowed_token(lAllowTokens, lTokens):
    bSkip = False
    for oAllowToken in lAllowTokens:
        for oToken in lTokens:
            if isinstance(oToken, oAllowToken):
                bSkip = True
                break
        if bSkip:
            break
    if bSkip:
        return True
    return False


def _comment_starts_line(lTokens):
    if len(lTokens) == 1:
        if token_is_comment(lTokens[0]):
            return True
    elif len(lTokens) == 2:
        if token_is_whitespace(lTokens[0]) and token_is_comment(lTokens[1]):
            return True
    return False
