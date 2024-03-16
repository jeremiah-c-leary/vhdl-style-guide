# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group import whitespace
from vsg.rules import utils


class rule_100(whitespace.Rule):
    """
    This rule checks for a single space after the **--**.

    |configuring_whitespace_after_comment_rules_link|

    **Violation**

    .. code-block:: vhdl

       --Comment 1
       --|Comment 2
       ---Comment
       ---------------------------

    **Fix**

    .. code-block:: vhdl

       -- Comment 1
       --|Comment 2
       ---Comment
       ---------------------------
    """

    def __init__(self):
        super().__init__()
        self.solution = "Undefined"
        self.phase = 2
        self.disable = False
        self.lTokens = [parser.comment]
        self.exceptions = ["--!", "--=", "--+", "--|", "---"]
        self.configuration.append("exceptions")
        self.patterns = ["--!", "--|"]
        self.configuration.append("patterns")
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lReturn = []
        lToi = oFile.get_tokens_matching(self.lTokens)
        for oToi in lToi:
            oToken = oToi.get_tokens()[0]
            if oToken.is_block_comment:
                continue
            if self.pattern_found(oToken):
                oToi.set_meta_data("type", "pattern")
                oToi.set_meta_data("pattern", self.get_matching_pattern(oToken))
                lReturn.append(oToi)
            elif not self.valid_comment(oToken):
                oToi.set_meta_data("type", "exception")
                lReturn.append(oToi)
        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            create_violation(self, oToi)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()

        sToken = lTokens[0].get_value()
        sNewToken = sToken[0 : dAction["index"]] + " " + sToken[dAction["index"] :]
        lTokens[0].set_value(sNewToken)
        oViolation.set_tokens(lTokens)

    def valid_comment(self, oToken):
        sToken = oToken.get_value()
        if len(sToken) == 2:
            return True
        if sToken.startswith("-- "):
            return True
        if self.exception_found(sToken):
            return True
        return False

    def exception_found(self, sToken):
        if sToken[0:3] in self.exceptions:
            return True
        return False

    def pattern_found(self, oToken):
        sToken = oToken.get_value()
        if len(sToken) < 4:
            return False
        for sPattern in self.patterns:
            if sToken.startswith(sPattern):
                if not sToken.startswith(sPattern + " "):
                    return True
        return False

    def get_matching_pattern(self, oToken):
        sToken = oToken.get_value()
        for sPattern in self.patterns:
            if sToken.startswith(sPattern):
                return sPattern
        return None


def create_violation_action_dict(sToken, iIndex):
    dReturn = {}
    dReturn["violation"] = True
    dReturn["index"] = iIndex
    dReturn["solution"] = create_solution(iIndex, sToken)
    return dReturn


def create_violation(self, oToi):
    if oToi.get_meta_data("type") == "pattern":
        iIndex = len(oToi.get_meta_data("pattern"))
    else:
        iIndex = 2
    dResults = create_violation_action_dict(oToi.get_tokens()[0].get_value(), iIndex)
    oViolation = violation.New(oToi.get_line_number(), oToi, dResults["solution"])
    oViolation.set_action(dResults)
    self.add_violation(oViolation)


def create_solution(iIndex, sComment):
    return 'Change "' + sComment[0 : iIndex + 1] + '" to "' + sComment[0:iIndex] + " " + sComment[iIndex] + '"'
