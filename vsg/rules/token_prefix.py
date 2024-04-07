# -*- coding: utf-8 -*-

import re

from vsg import parser, violation
from vsg.rule_group import naming
from vsg.rules import utils as rules_utils


class token_prefix(naming.Rule):
    """
    Checks the prefix for words.

    Parameters
    ----------

    name : string
       The group the rule belongs to.

    identifier : string
       unique identifier.  Usually in the form of 00N.

    lTokens : list of parser object types
       object types to check the prefix

    lPrefixes : string list
       acceptable prefixes
    """

    def __init__(self, lTokens):
        super().__init__()
        self.lTokens = lTokens
        self.prefixes = None
        self.configuration.append("prefixes")
        self.fixable = False
        self.disable = True
        self.exceptions = []
        self.configuration.append("exceptions")
        self.regexp_exceptions = []

    def _get_tokens_of_interest(self, oFile):
        return oFile.get_tokens_matching(self.lTokens)

    def _analyze(self, lToi):
        self.generate_regexp_exceptions()

        lPrefixLower = []
        for sPrefix in self.prefixes:
            lPrefixLower.append(sPrefix.lower())

        for oToi in lToi:
            lTokens = oToi.get_tokens()
            sToken = lTokens[0].get_lower_value()

            if self.exception_found(sToken):
                continue

            bValid = False
            for sPrefix in lPrefixLower:
                if sToken.startswith(sPrefix.lower()):
                    bValid = True
            if not bValid:
                sSolution = "Prefix " + lTokens[0].get_value() + " with one of the following: " + ", ".join(self.prefixes)
                oViolation = violation.New(oToi.get_line_number(), oToi, sSolution)
                self.add_violation(oViolation)

    def _fix_violation(self, oViolation):
        lTokens = oViolation.get_tokens()
        if oViolation.get_action() == "remove_whitespace":
            oViolation.set_tokens([lTokens[1]])
        elif oViolation.get_action() == "adjust_whitespace":
            lTokens[0].set_value(lTokens[1].get_indent() * self.indent_size * " ")
            oViolation.set_tokens(lTokens)
        elif oViolation.get_action() == "add_whitespace":
            rules_utils.insert_whitespace(lTokens, 0, lTokens[0].get_indent() * self.indent_size)
            oViolation.set_tokens(lTokens)

    def generate_regexp_exceptions(self):
        for exception in self.exceptions:
            regexp = re.compile(exception, re.IGNORECASE)
            self.regexp_exceptions.append(regexp)

    def exception_found(self, sToken):
        for regexp in self.regexp_exceptions:
            if regexp.match(sToken) is not None:
                return True
        return False
