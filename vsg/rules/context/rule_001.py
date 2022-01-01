
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.context_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of the **context** keyword.

    **Violation**

    .. code-block:: vhdl

         context c1 is

         library ieee;

    **Fix**

    .. code-block:: vhdl

       context c1 is

         library ieee;
    '''

    def __init__(self):
        token_indent.__init__(self, 'context', '001', lTokens)
