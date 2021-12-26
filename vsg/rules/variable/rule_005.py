
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_005(single_space_after_token):
    '''
    This rule checks there is a single space after the colon.

    **Violation**

    .. code-block:: vhdl

       variable count   :integer;
       variable counter :     integer;

    **Fix**

    .. code-block:: vhdl

       variable count   : integer;
       variable counter : integer;
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'variable', '005', lTokens)
        self.solution = 'Ensure only a single space after the colon.'
