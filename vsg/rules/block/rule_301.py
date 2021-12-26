
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.block_statement.begin_keyword)


class rule_301(token_indent):
    '''
    This rule checks the indent of the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       block_label : block is

         begin

    **Fix**

    .. code-block:: vhdl

       block_label : block is

       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'block', '301', lTokens)
