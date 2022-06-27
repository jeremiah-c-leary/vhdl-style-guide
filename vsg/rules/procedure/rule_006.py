
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.close_parenthesis)


class rule_006(token_indent):
    '''
    This rule checks the indent of the closing parenthesis if it is on its own line.

    **Violation**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal d : out std_logic
         ) is


    **Fix**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal d : out std_logic
       ) is
    '''

    def __init__(self):
        token_indent.__init__(self, 'procedure', '006', lTokens)
