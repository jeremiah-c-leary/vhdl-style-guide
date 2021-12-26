
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.enumeration_type_definition.close_parenthesis)


class rule_016(token_indent):
    '''
    This rule checks the indent of the closing parenthesis on multiline types.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         type state_machine is (
           idle, write, read, done
           );

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         type state_machine is (
           idle, write, read, done
         );

       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'type', '016', lTokens)
