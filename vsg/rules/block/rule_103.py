# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.block_statement.label_colon, token.block_statement.block_keyword])


class rule_103(Rule):
    """
    This rule checks for a single space after the colon and before the **block** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label :block is

    **Fix**

    .. code-block:: vhdl

       block_label : block is
    """

    def __init__(self):
        super().__init__(lTokens)
