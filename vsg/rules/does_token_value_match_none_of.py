# -*- coding: utf-8 -*-

from vsg.rules import does_token_value_match_one_of as Rule


class does_token_value_match_none_of(Rule.does_token_value_match_one_of):
    """
    Checks if a token value matches none of provided regex patterns.
    """

    def __init__(self, oToken):
        super().__init__(oToken)

    def _check_for_violation(self, sToken, lRegexNames):
        return not self._token_matches_at_least_one(sToken, lRegexNames)
