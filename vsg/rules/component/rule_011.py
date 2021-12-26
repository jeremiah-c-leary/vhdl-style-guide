
from vsg.rules import single_space_between_tokens

from vsg.token import component_declaration as token


class rule_011(single_space_between_tokens):
    '''
    This rule checks for single space after the **end** keyword.

    **Violation**

    .. code-block:: vhdl

       end   component fifo;

    **Fix**

    .. code-block:: vhdl

       end component fifo;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'component', '011', token.end_keyword, token.end_component_keyword)
        self.solution = 'Reduce spaces between *end* keyword and *component* keyword.'
