
from vsg import token

from vsg.rules import move_token_left_to_next_non_whitespace_token as Rule

oToken = token.entity_declaration.semicolon


class rule_025(Rule):
    '''
    This rule checks the semicolon is not on its own line.

    **Violation**

    .. code-block:: vhdl

       end entity;

       end entity
       ;

    **Fix**

    .. code-block:: vhdl

       end entity;

       end entity;
    '''

    def __init__(self):
        Rule.__init__(self, 'entity', '025', oToken)
        self.bInsertWhitespace = False
        self.subphase = 3
