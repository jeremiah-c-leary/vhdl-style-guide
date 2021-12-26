
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.port_clause.port_keyword)


class rule_002(token_indent):
    '''
    This rule checks the indent of the **port** keyword.

    **Violation**

    .. code-block:: vhdl

       entity FIFO is
       port (

    **Fix**

    .. code-block:: vhdl

       entity FIFO is
         port (
    '''

    def __init__(self):
        token_indent.__init__(self, 'port', '002', lTokens)
