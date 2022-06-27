
from vsg import token

from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

oToken = token.port_clause.semicolon


class rule_027(Rule):
    '''
    This rule checks the semicolon is not on its own line.

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port (
           I_WIDTH : in integer
         )
         ;

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         generic (
           I_WIDTH : in integer
         );
    '''

    def __init__(self):
        Rule.__init__(self, 'port', '027', oToken)
        self.bInsertWhitespace = False
