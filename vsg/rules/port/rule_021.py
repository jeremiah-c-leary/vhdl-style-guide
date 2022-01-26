
from vsg.rules import move_token_next_to_another_token

from vsg.token import port_clause as token


class rule_021(move_token_next_to_another_token):
    '''
    This rule checks the **port** keyword is on the same line as the (.

    **Violation**

    .. code-block:: vhdl

       port
       (

    **Fix**

    .. code-block:: vhdl

       port (
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'port', '021', token.port_keyword, token.open_parenthesis)
        self.solution = 'Move the ( to the same line as the *port* keyword.'
