
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.constant_declaration.colon)


class rule_006(whitespace_before_token):
    '''
    This rule checks for at least a single space before the colon.

    **Violation**

    .. code-block:: vhdl

       constant size: integer := 1;
       constant width     : integer := 32;

    **Fix**

    .. code-block:: vhdl

       constant size : integer := 1;
       constant width     : integer := 32;
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'constant', '006', lTokens)
        self.solution = 'Ensure at least one space before colon.'
