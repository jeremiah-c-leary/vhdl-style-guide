
from vsg.rules import single_space_between_tokens

from vsg.token import context_declaration as token


class rule_017(single_space_between_tokens):
    '''
    This rule checks for a single space between the context identifier and the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       context c1    is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context', '017', token.identifier, token.is_keyword)
        self.solution = 'Reduce spaces between identifier and *is* keyword to a single space.'
