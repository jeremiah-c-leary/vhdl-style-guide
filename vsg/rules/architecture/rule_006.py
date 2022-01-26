
from vsg.rules import move_token_next_to_another_token

from vsg.token import architecture_body as token


class rule_006(move_token_next_to_another_token):
    '''
    This rule checks the **is** keyword is on the same line as the **architecture** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo
         is

       architecture rtl of fifo

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

       architecture rtl of fifo is
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'architecture', '006', token.entity_name, token.is_keyword)
        self.solution = 'Ensure *is* keyword is on the same line as the entity name.'
