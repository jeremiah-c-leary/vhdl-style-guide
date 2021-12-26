
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.component_declaration.component_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indentation of the **component** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin

       component fifo is

            component ram is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin

         component fifo is

         component ram is
    '''

    def __init__(self):
        token_indent.__init__(self, 'component', '001', lTokens)
