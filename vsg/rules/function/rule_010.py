
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.function_specification.designator)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_010(consistent_token_case):
    '''
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
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'function', '010', lTokens, lIgnore)
