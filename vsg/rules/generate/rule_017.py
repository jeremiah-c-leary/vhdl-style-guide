# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_prefix

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.case_generate_statement.end_generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.end_generate_label)
lTokens.append(token.if_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.end_generate_label)


class rule_017(token_prefix):
    """
    This rule checks for valid prefixes on generate statement labels.
    The default prefix is *gen_*.

    |configuring_prefix_and_suffix_rules_link|

    **Violation**

    .. code-block:: vhdl

       label : case condition generate

    **Fix**

    .. code-block:: vhdl

       gen_label : case condition generate
    """

    def __init__(self):
        super().__init__(lTokens)
        self.prefixes = ["gen_"]
