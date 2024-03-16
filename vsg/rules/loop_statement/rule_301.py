# -*- coding: utf-8 -*-

from vsg import token
from vsg.rules import token_indent

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_301(token_indent):
    """
    This rule checks the indentation of the loop label if it exists.

    **Violation**

    .. code-block:: vhdl

       fifo_proc : process () is
       begin

           LOOP_LABEL : loop

         end loop;

       end process;

    **Fix**

    .. code-block:: vhdl

       fifo_proc : process () is
       begin

         LOOP_LABEL : loop

         end loop;

       end process;
    """

    def __init__(self):
        super().__init__(lTokens)
