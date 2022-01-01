

from vsg.rules import move_token_next_to_another_token

from vsg.token import architecture_body as token


class rule_005(move_token_next_to_another_token):
    '''
    This rule checks the **of** keyword is on the same line as the **architecture** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture rtl
         of fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of
       fifo is
    '''

    def __init__(self):
        move_token_next_to_another_token.__init__(self, 'architecture', '005', token.identifier, token.of_keyword)
        self.solution = 'Ensure *of* keyword is on the same line as the architecture identifier.'
