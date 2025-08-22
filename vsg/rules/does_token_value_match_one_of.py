# -*- coding: utf-8 -*-

import re

from vsg import violation
from vsg.rule_group import naming


class does_token_value_match_one_of(naming.Rule):
    """
    Checks if a token value matches one of provided regex patterns.
    """

    def __init__(self, token):
        super().__init__()
        self.names = []
        self.fixable = False
        self.disable = True
        self.configuration.append("names")
        self.token = token
        self.configuration_documentation_link = None
        self.regexp_names = []

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([self.token])

    def _analyze(self, lToi):
        self.generate_regexp_names()

        self.solution = self._get_solution(None)
        lower_names = []
        for sName in self.names:
            lower_names.append(sName.lower())

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sToken = lTokens[0].get_lower_value()
            if not self.name_found(sToken):
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))

    def generate_regexp_names(self):
        self.regexp_names = []
        for name in self.names:
            regexp = re.compile(name, re.IGNORECASE)
            self.regexp_names.append(regexp)

    def name_found(self, sToken):
        for regexp in self.regexp_names:
            if regexp.fullmatch(sToken) is not None:
                return True
        return False
