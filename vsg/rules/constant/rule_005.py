
from vsg.rules import single_space_after_token

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.colon)


class rule_005(single_space_after_token):
    '''
    This rule checks for a single space after the colon.

    **Violation**

    .. code-block:: vhdl

       constant size  :integer := 1;
       constant width :     integer := 32;

    **Fix**

    .. code-block:: vhdl

       constant size  : integer := 1;
       constant width : integer := 32;
    '''

    def __init__(self):
        single_space_after_token.__init__(self, 'constant', '005', lTokens)
