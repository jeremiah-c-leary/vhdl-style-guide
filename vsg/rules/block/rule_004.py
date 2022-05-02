
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_004(split_line_at_token):
    '''
    This rule checks the **begin** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       block is begin

    **Fix**

    .. code-block:: vhdl

       block is
       begin
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'block', '004', lTokens)
        self.solution = 'Move *begin* keyword and code after it to the next line'
