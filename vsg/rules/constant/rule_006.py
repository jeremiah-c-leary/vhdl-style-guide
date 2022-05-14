
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.constant_declaration.colon)


class rule_006(Rule):
    '''
    This rule checks for at least a single space before the colon.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'constant', '006', lTokens)
        self.number_of_spaces = '>=1'
