# -*- coding: utf-8 -*-


from vsg import violation
from vsg.rule_group import naming


class is_token_value_one_of(naming.Rule):
    """
    Checks if a token value is in a list of provided values.
    """

    def __init__(self, token):
        super().__init__()
        self.names = []
        self.fixable = False
        self.disable = True
        self.configuration.append("names")
        self.token = token
        self.configuration_documentation_link = None

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching([self.token])

    def _analyze(self, lToi):
        self.solution = self._get_solution(None)
        lower_names = []
        for sName in self.names:
            lower_names.append(sName.lower())

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            if not lTokens[0].get_lower_value() in lower_names:
                self.add_violation(violation.New(oToi.get_line_number(), oToi, self.solution))
