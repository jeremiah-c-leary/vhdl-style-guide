# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.case_generate_statement.end_generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.end_generate_label)
lTokens.append(token.if_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.end_generate_label)


class rule_600(token_suffix):
    """
    This rule checks for valid suffixes on generate statement labels.
    The default suffix is *_gen*.

    |configuring_prefix_and_suffix_rules_link|

    [Violation]

       label : case condition generate

    [Fix]

       label_gen : case condition generate
    """

    def __init__(self):
        super().__init__(lTokens)
        self.suffixes = ["_gen"]
