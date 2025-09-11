# -*- coding: utf-8 -*-

import re

from vsg import violation
from vsg.rule_group import naming


class does_token_value_match_one_of(naming.Rule):
    """
    Checks if a token value matches one of provided regex patterns.
    """

    def __init__(self, oToken):
        super().__init__()
        self.names = []
        self.fixable = False
        self.disable = True
        self.configuration.append("names")
        self.token = oToken
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([self.token])

    def _analyze(self, lToi):
        self.solution = self._get_solution(None)
        lRegexNames = [re.compile(name, re.IGNORECASE) for name in self.names]

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if self._check_for_violation(lTokens[0].get_lower_value(), lRegexNames):
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def _check_for_violation(self, sToken, lRegexNames):
        return self._token_matches_at_least_one(sToken, lRegexNames)

    def _token_matches_at_least_one(self, sToken, lRegexNames):
        for regex in lRegexNames:
            if regex.fullmatch(sToken) is not None:
                return False
        return True
