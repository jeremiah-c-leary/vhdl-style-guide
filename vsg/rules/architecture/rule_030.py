
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token


class rule_030(single_space_between_tokens):
    '''
    This rule checks for a single space between **architecture** and the name.

    **Violation**

    .. code-block:: vhdl

       architecture    rtl of fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '030', token.architecture_keyword, token.identifier)
        self.solution = 'Reduce spaces between *architecture* keyword and identifier to a single space.'
