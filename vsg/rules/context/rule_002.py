
from vsg.rules import single_space_between_tokens

from vsg.token import context_declaration as token


class rule_002(single_space_between_tokens):
    '''
    This rule checks for a single space between the **context** keyword and the context identifier.

    **Violation**

    .. code-block:: vhdl

       context   c1 is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context', '002', token.context_keyword, token.identifier)
        self.solution = 'Reduce spaces between *context* keyword and identifier.'
