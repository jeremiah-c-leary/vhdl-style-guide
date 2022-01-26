
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_011(single_space_between_tokens):
    '''
    This rule checks for a single space after the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       end    entity fifo;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '011', token.end_keyword, token.end_entity_keyword)
        self.solution = 'Reduce spaces between *end* keyword and *entity* keyword to a single space.'
