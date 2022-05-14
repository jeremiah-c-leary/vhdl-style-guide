
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.variable_declaration.colon)


class rule_006(Rule):
    '''
    This rule checks for at least a single space before the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       variable count: integer;
       variable counter : integer;

    **Fix**

    .. code-block:: vhdl

       variable count : integer;
       variable counter : integer;
    '''
    def __init__(self):
        Rule.__init__(self, 'variable', '006', lTokens)
        self.number_of_spaces = '>=1'
