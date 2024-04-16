# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.constant_declaration.assignment_operator)


class rule_100(Rule):
    """
    This rule checks for a single space after the := assignment in constant declarations.
    Having a space makes it clearer where the assignment occurs on the line.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       constant size : integer :=1;
       constant width : t_type :=(

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
       constant width : t_type := (
    """

    def __init__(self):
        super().__init__(lTokens)
