
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.function_specification.pure_keyword)
lTokens.append(token.function_specification.impure_keyword)
lTokens.append(token.function_specification.function_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indentation of the **function** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture RTL of FIFO is

           function overflow (a: integer) return integer is


       function underflow (a: integer) return integer is

       begin

    **Fix**

    .. code-block:: vhdl

       architecture RTL of FIFO is

         function overflow (a: integer) return integer is

         function underflow (a: integer) return integer is

       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'function', '001', lTokens)
