# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_case_in_range_bounded_by_tokens as Rule

lTokens = []
lTokens.append(token.choice.others_keyword)

oStart = token.aggregate.open_parenthesis
oEnd = token.aggregate.close_parenthesis


class rule_500(Rule):
    """
    This rule checks the *others* keyword in aggregates has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal counter : t_counter := (OTHERS => '1');

    **Fix**

    .. code-block:: vhdl

       signal counter : t_counter := (others => '1');
    """

    def __init__(self):
        super().__init__(lTokens, oStart, oEnd)
        self.groups.append("case::keyword")
