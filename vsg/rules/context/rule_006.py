
from vsg.rules import move_token_next_to_another_token

from vsg.token import context_declaration as token


class rule_006(move_token_next_to_another_token):
    '''
    This rule checks the **is** keyword is on the same line as the context identifier.

    **Violation**

    .. code-block:: vhdl

       context c1
         is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'context', '006', token.identifier, token.is_keyword)
        self.subphase = 2
        self.solution = 'Move *is* keyword next to context identifier'
