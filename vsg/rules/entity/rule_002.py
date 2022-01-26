
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_002(single_space_between_tokens):
    '''
    This rule checks for a single space after the **entity** keyword.

    **Violation**

    .. code-block:: vhdl

       entity    fifo is

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '002', token.entity_keyword, token.identifier)
        self.solution = 'Reduce spaces between *entity* keyword and identifier to a single space.'
