# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import blank_line_below_line_ending_with_token

lTokens = []
lTokens.append(token.if_statement.semicolon)


class rule_030(blank_line_below_line_ending_with_token):
    """
    This rule checks a single blank line after the **end if**.
    In the case of nested **if** statements, the rule will be enforced on the last **end if**.

    |configuring_blank_lines_link|

    **Violation**

    .. code-block:: vhdl

       if (A = '1') then
         B <= '0';
       end if;
       C <= '1';

    **Fix**

    .. code-block:: vhdl

       if (A = '1') then
         B <= '0';
       end if;

       C <= '1';
    """

    def __init__(self):
        super().__init__(lTokens)
        self.lHierarchyLimits = [0]
