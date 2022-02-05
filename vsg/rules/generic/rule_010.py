
from vsg.rules import move_token as Rule

from vsg import token

oToken = token.generic_clause.close_parenthesis


class rule_010(Rule):
    '''
    This rule checks the location of the closing ")" character for the generic clause.

    The default location is on a line by itself.

    |configuring_move_token_rules_link|

    **Violation**

    .. code-block:: vhdl

       g_depth : integer := 512);

    **Fix**

    .. code-block:: vhdl

         g_depth : integer := 512
       );
    '''

    def __init__(self):
        Rule.__init__(self, 'generic', '010', oToken)
        self.preserve_comment = True
