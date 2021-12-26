
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.type_keyword)
lTokens.append(token.full_type_declaration.type_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of the **type** declaration.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

           type state_machine is (idle, write, read, done);

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         type state_machine is (idle, write, read, done);

       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'type', '001', lTokens)
