
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_007(single_space_between_tokens):
    '''
    This rule checks for a single space before the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       entity fifo    is

    **Fix**

    .. code-block:: vhdl

       entity fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '007', token.identifier, token.is_keyword)
        self.solution = 'Reduce spaces between identifier and *is* keyword to a single space.'
