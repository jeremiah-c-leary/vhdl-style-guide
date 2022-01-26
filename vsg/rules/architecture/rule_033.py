
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token


class rule_033(single_space_between_tokens):
    '''
    This rule checks for a single space between the entity_name and the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo    is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '033', token.entity_name, token.is_keyword)
        self.solution = 'Reduce spaces between the entity_name and the *is* keyword to a single space.'
