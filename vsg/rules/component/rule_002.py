
from vsg.rules import single_space_between_tokens

from vsg.token import component_declaration as token


class rule_002(single_space_between_tokens):
    '''
    This rule checks for a single space after the **component** keyword.

    **Violation**

    .. code-block:: vhdl

       component    fifo is

    **Fix**

    .. code-block:: vhdl

       component fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'component', '002', token.component_keyword, token.identifier)
        self.solution = 'Reduce spaces between *component* keyword and identifier.'
