# -*- coding: utf-8 -*-

from vsg import violation
from vsg.rule_group import structure


class Rule(structure.Rule):
    """
    This rule checks if a token pair does not exist.
    """

    def __init__(self, oFirstToken, oSecondToken):
        super().__init__()
        self.oFirstToken = oFirstToken
        self.oSecondToken = oSecondToken
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        lReturn = []

        lFirstTokens = oFile.get_tokens_matching([self.oFirstToken])
        lSecondTokens = oFile.get_tokens_matching([self.oSecondToken])

        iPreviousIndex = 0
        for oSecondToken in lSecondTokens:
            iCurrentIndex = oSecondToken.get_start_index()
            if not first_token_before_second_token(lFirstTokens, iCurrentIndex, iPreviousIndex):
                lReturn.append(oSecondToken)
            iPreviousIndex = iCurrentIndex

        return lReturn

    def _analyze(self, lToi):
        for oToi in lToi:
            oViolation = violation.New(oToi.get_line_number(), oToi, self.solution)
            self.add_violation(oViolation)


def first_token_before_second_token(lFirstTokens, iCurrentIndex, iPreviousIndex):
    for oFirstToken in lFirstTokens:
        iFirstIndex = oFirstToken.get_start_index()
        if iPreviousIndex < iFirstIndex and iFirstIndex < iCurrentIndex:
            return True
    return False
