# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.subtype_declaration.subtype_keyword)


class rule_201(previous_line):
    """
    This rule checks for blank lines or comments above the **subtype** declaration.

    |configuring_previous_line_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal wr_en : std_logic;
       subtype counter is unsigned(4 downto 0);

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic;

       subtype counter is unsigned(4 downto 0);
    """

    def __init__(self):
        super().__init__(lTokens)
