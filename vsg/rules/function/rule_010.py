# -*- coding: utf-8 -*-

from vsg import parser, token
from vsg.rules import consistent_token_case as Rule

lTokens = []
lTokens.append(token.function_specification.designator)

lNames = []
lNames.append(token.todo.name)
lNames.append(parser.todo)


class rule_010(Rule):
    """
    This rule checks for consistent capitalization of function names.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         function func_1 ()

       begin

         OUT1 <= Func_1;

         PROC1 : process () is
         begin

            sig1 <= FUNC_1;

         end process;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         function func_1 ()

       begin

         OUT1 <= func_1;

         PROC1 : process () is
         begin

            sig1 <= func_1;

         end process;

       end architecture rtl;
    """

    def __init__(self):
        super().__init__(lTokens, lNames)
        self.bIncludeDeclarativePartNames = True
