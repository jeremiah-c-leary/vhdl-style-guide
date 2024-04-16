# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.loop_statement.end_keyword)


class rule_302(token_indent):
    """
    This rule checks the indentation of the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       fifo_proc : process () is
       begin

         for index in 4 to 23 loop

            end loop;

       end process;

    **Fix**

    .. code-block:: vhdl

       fifo_proc : process () is
       begin

         for index in 4 to 23 loop

         end loop;

       end process;
    """

    def __init__(self):
        super().__init__(lTokens)
