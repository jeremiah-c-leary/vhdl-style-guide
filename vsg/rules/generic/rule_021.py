
from vsg import token

from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

oToken = token.generic_clause.semicolon


class rule_021(Rule):
    '''
    This rule checks the semicolon is not on its own line.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic (
           G_WIDTH : integer
         )
         ;

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic (
           G_WIDTH : integer
         );
    '''

    def __init__(self):
        Rule.__init__(self, 'generic', '021', oToken)
        self.bInsertWhitespace = False
