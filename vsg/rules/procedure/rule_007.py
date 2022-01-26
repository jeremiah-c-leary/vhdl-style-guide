
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.procedure_specification.designator)

lIgnore = []
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_007(consistent_token_case):
    '''
    This rule checks for consistent capitalization of procedure names.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of entity1 is

         procedure average_samples (
           constant a : in integer;
           signal d : out std_logic
         ) is

       begin

         proc1 : process () is
         begin

           Average_samples();

         end process proc1;

       end architecture rtl;

    **Fix**

    .. code-block:: vhdl

       architecture rtl of entity1 is

         procedure average_samples (
           constant a : in integer;
           signal d : out std_logic
         ) is

       begin

         proc1 : process () is
         begin

           average_samples();

         end process proc1;

       end architecture RTL;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'procedure', '007', lTokens, lIgnore)
