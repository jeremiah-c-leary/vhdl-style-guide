
from vsg.rules import move_token_next_to_another_token as Rule

from vsg.token import entity_declaration as token


class rule_023(Rule):
    '''
    This rule checks the end **entity** keyword is on the same line as the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       end entity;

       end
         entity;

    **Fix**

    .. code-block:: vhdl

       end entity;

       end entity;
    '''

    def __init__(self):
        Rule.__init__(self, 'entity', '023', token.end_keyword, token.end_entity_keyword)
        self.subphase = 1
        self.solution = 'Move identifier next to *entity* keyword'
