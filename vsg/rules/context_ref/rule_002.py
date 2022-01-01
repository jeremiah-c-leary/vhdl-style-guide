
from vsg.rules import single_space_between_tokens

from vsg.token import context_reference as token


class rule_002(single_space_between_tokens):
    '''
    This rule checks for a single space between the **context** keyword and the context selected name.

    **Violation**

    .. code-block:: vhdl

       context   c1;

    **Fix**

    .. code-block:: vhdl

       context c1;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context_ref', '002', token.keyword, token.selected_name)
        self.solution = 'Reduce spaces between *context* keyword and selected_name.'
