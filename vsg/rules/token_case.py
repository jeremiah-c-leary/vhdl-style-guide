# -*- coding: utf-8 -*-

import re

from vsg.rule_group import case
from vsg.rules import case_utils, utils


class token_case(case.Rule):
    """
    Checks the case for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of token types
       The token types to check the case on.
    """

    def __init__(self, lTokens):
        super().__init__()
        self.solution = None
        self.phase = 6
        self.case = "lower"
        self.configuration.append("case")
        self.lTokens = lTokens
        self.prefix_exceptions = []
        self.suffix_exceptions = []
        self.case_exceptions = []
        self.regex = ""
        self.oRegex = None

    def _get_tokens_of_interest(self, oFile):
        self.case_exceptions_lower = utils.lowercase_list(self.case_exceptions)
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        check_prefix = case_utils.is_exception_enabled(self.prefix_exceptions)
        check_suffix = case_utils.is_exception_enabled(self.suffix_exceptions)
        check_whole = case_utils.is_exception_enabled(self.case_exceptions)
        self.oRegex = re.compile(self.regex)
        for oToi in lToi:
            oViolation = case_utils.check_for_case_violation(oToi, self, check_prefix, check_suffix, check_whole)
            if oViolation is not None:
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        dAction = oViolation.get_action()
        if dAction["value"] is not None:
            lTokens[0].set_value(dAction["value"])
            oViolation.set_tokens(lTokens)
