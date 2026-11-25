# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.block_statement.guard_close_parenthesis, token.block_statement.is_keyword])


class rule_105(Rule):
    """
    This rule checks for a single space between the guard close parenthesis and the **is** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       block_label : block (guard_condition)is

    **Fix**

    .. code-block:: vhdl

       block_label : block (guard_condition) is
    """

    def __init__(self):
        super().__init__(lTokens)
