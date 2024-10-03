# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.interface_unknown_declaration.assignment)


class rule_101(Rule):
    """
    This rule checks for a single space after the assignment.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       I_WIDTH : in integer :=32;
       I_DEPTH : in integer :=    256;

    **Fix**

    .. code-block:: vhdl

       I_WIDTH : in integer := 32;
       I_DEPTH : in integer := 256;
    """

    def __init__(self):
        super().__init__(lTokens)
