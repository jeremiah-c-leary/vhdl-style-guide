
from vsg.rules import move_token_next_to_another_token

from vsg.token import entity_declaration as token


class rule_005(move_token_next_to_another_token):
    '''
    This rule checks the **is** keyword is on the same line as the **entity** keyword.

    **Violation**

    .. code-block:: vhdl

       entity fifo

       entity fifo
         is

    **Fix**

    .. code-block:: vhdl

       entity fifo is

       entity fifo is
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'entity', '005', token.identifier, token.is_keyword)
        self.subphase = 2
        self.solution = 'Move *is* keyword next to identifier'
