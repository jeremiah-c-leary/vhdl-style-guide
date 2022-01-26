
from vsg.rules import single_space_between_tokens

from vsg.token import component_declaration as token


class rule_013(single_space_between_tokens):
    '''
    This rule checks for a single space after the **component** keyword in the **end component** line.

    **Violation**

    .. code-block:: vhdl

       end component    fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'component', '013', token.end_component_keyword, token.component_simple_name)
        self.solution = 'Reduce spaces between *end* keyword and *component* keyword.'
