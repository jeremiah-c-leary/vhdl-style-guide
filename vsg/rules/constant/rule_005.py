
from vsg.rules.whitespace_after_token import Rule

from vsg import token

lTokens = []
lTokens.append(token.constant_declaration.colon)


class rule_005(Rule):
    '''
    This rule checks for a single space after the colon.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'constant', '005', lTokens)
