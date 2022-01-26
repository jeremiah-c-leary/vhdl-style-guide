
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token


class rule_031(single_space_between_tokens):
    '''
    This rule checks for a single space between the name and the **of** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture rtl    of fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '031', token.identifier, token.of_keyword)
        self.solution = 'Reduce spaces between identifier and *of* keyword to a single space.'
