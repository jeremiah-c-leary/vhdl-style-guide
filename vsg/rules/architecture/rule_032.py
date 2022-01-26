
from vsg.rules import single_space_between_tokens

from vsg.token import architecture_body as token


class rule_032(single_space_between_tokens):
    '''
    This rule checks for a single space between the **of** keyword and the entity_name.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of    fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'architecture', '032', token.of_keyword, token.entity_name)
        self.solution = 'Reduce spaces between *of* keyword and entity_name to a single space.'
