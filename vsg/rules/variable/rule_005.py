
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_005(Rule):
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
        Rule.__init__(self, 'variable', '005', lTokens)
        self.solution = 'Ensure only a single space after the colon.'
