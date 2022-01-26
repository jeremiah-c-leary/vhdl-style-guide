
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.procedure_specification.designator)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_507(consistent_token_case):
    '''
    This rule checks for consistent capitalization of procedure names.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         procedure average_samples is
         begin
         end procedure average_samples

       begin

         Average_samples;

         PROC1 : process () is
         begin

            AVERAGE_SAMPLES;

         end process;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         procedure average_samples is
         begin
         end procedure average_samples

       begin

         average_samples;

         PROC1 : process () is
         begin

            average_samples;

         end process;

       end architecture rtl;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'procedure', '507', lTokens, lIgnore)
