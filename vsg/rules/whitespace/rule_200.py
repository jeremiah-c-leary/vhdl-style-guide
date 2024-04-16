# -*- coding: utf-8 -*-

from vsg import parser, violation
from vsg.rule_group.blank_line import Rule
from vsg.vhdlFile import utils


class rule_200(Rule):
    """
    This rule enforces a maximum number of consecutive blank lines.

    |configuring_consecutive_blank_line_rules|

    **Violation**

    .. code-block:: vhdl

       a <= b;


       c <= d;

    **Fix**

    .. code-block:: vhdl

       a <= b;

       c <= d;
    """

    def __init__(self):
        Rule.__init__(self)
        self.blank_lines_allowed = 1
        self.configuration.append("blank_lines_allowed")
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        return [oFile.get_all_tokens()]

    def _analyze(self, lToi):
        oToi = lToi[0]
        iLine, lTokens = utils.get_toi_parameters(oToi)
        iCount = 0
        for iToken, oToken in enumerate(lTokens[: len(lTokens) - 1]):
            iLine = utils.increment_line_number(iLine, oToken)

            if isinstance(oToken, parser.blank_line):
                if iCount == 0:
                    iLineNumber = iLine
                    iStartToken = iToken
                iCount += 1

            if isinstance(oToken, parser.carriage_return):
                if not isinstance(lTokens[iToken + 1], parser.blank_line):
                    if iCount > self.blank_lines_allowed:
                        sSolution = "Remove " + str(iCount - self.blank_lines_allowed) + " blank line(s) below"
                        lExtractedTokens = oToi.extract_tokens(iStartToken, iToken)
                        oViolation = violation.New(iLineNumber, lExtractedTokens, sSolution)
                        dAction = {}
                        dAction["remove"] = iCount - self.blank_lines_allowed
                        oViolation.set_action(dAction)
                        self.add_violation(oViolation)

                    iCount = 0

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        lTokens = lTokens[2 * dAction["remove"] :]
        oViolation.set_tokens(lTokens)
