
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generic_clause.close_parenthesis)


class rule_008(token_indent):
    '''
    This rule checks the indent of the closing parenthesis.

    **Violation**

    .. code-block:: vhdl

       g_depth : integer := 512
       );

    **Fix**

    .. code-block:: vhdl

         g_depth : integer := 512
       );
    '''

    def __init__(self):
        token_indent.__init__(self, 'generic', '008', lTokens)
