# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent as Rule

lTokens = []
lTokens.append(token.alias_declaration.alias_keyword)


class rule_300(Rule):
    """
    This rule checks the indent of the **alias** keyword.

    **Violation**

    .. code-block:: vhdl

       signal sig1 : integer;

         alias is name;

    **Fix**

    .. code-block:: vhdl

       signal sig1 : integer;

       alias is name;
    """

    def __init__(self):
        super().__init__(lTokens)
