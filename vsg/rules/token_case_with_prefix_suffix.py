# -*- coding: utf-8 -*-

from vsg import rules


class token_case_with_prefix_suffix(rules.token_case):
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
        super().__init__(lTokens=lTokens)
        self.configuration.append("prefix_exceptions")
        self.configuration.append("suffix_exceptions")
        self.configuration.append("case_exceptions")
        self.configuration.append("regex")
