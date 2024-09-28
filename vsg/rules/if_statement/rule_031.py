# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import previous_line

lTokens = []
lTokens.append(token.if_statement.if_keyword)


class rule_031(previous_line):
    """
    This rule checks for blank lines or comments above the **if** keyword.
    In the case of nested **if** statements, the rule will be enforced on the first **if**.

    |configuring_previous_line_rules_link|

    The default style is :code:`no_code`.

    **Violation**

    .. code-block:: vhdl

       C <= '1';
       if (A = '1') then
         B <= '0';
       end if;

       -- This is a comment
       if (A = '1') then
         B <= '0';
       end if;

    **Fix**

    .. code-block:: vhdl

       C <= '1';

       if (A = '1') then
         B <= '0';
       end if;

       -- This is a comment
       if (A = '1') then
         B <= '0';
       end if;
    """

    def __init__(self):
        super().__init__(lTokens)
        self.lHierarchyLimits = [0]
        self.style = "no_code"
