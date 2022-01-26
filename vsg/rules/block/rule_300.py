
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_300(token_indent):
    '''
    This rule checks the indent of the block label.

    **Violation**

    .. code-block:: vhdl

       a <= b;

          block_label : block is

    **Fix**

    .. code-block:: vhdl

       a <= b;

       block_label : block is
    '''

    def __init__(self):
        token_indent.__init__(self, 'block', '300', lTokens)
