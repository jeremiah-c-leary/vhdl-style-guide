# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.block_statement.block_label, token.block_statement.label_colon])


class rule_102(Rule):
    """
    This rule checks for a single space after the block label.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label: block is

    **Fix**

    .. code-block:: vhdl

       block_label : block is
    """

    def __init__(self):
        super().__init__(lTokens)
