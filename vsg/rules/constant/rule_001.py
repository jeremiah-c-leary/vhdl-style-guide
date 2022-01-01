
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.constant_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of a constant declaration.

    **Violation**

    .. code-block:: vhdl

       architecture RTL of FIFO is

       constant size : integer := 1;
           constant width : integer := 32

    **Fix**

    .. code-block:: vhdl

       architecture RTL of FIFO is

         constant size : integer := 1;
         constant width : integer := 32
    '''

    def __init__(self):
        token_indent.__init__(self, 'constant', '001', lTokens)
