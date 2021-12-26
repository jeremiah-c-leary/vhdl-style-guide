
from vsg.rules import single_space_between_tokens

from vsg.token import entity_declaration as token


class rule_013(single_space_between_tokens):
    '''
    This rule checks for a single space after the **entity** keyword in the closing of the entity declaration.

    **Violation**

    .. code-block:: vhdl

       end entity    fifo;

    **Fix**

    .. code-block:: vhdl

       end entity fifo;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'entity', '013', token.end_entity_keyword, token.entity_simple_name)
        self.solution = 'Reduce spaces between *entity* keyword and the entity simple name to a single space.'
