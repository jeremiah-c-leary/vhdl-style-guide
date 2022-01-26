
from vsg.rules import single_space_between_tokens

from vsg.token import context_declaration as token


class rule_018(single_space_between_tokens):
    '''
    This rule checks for a single space between the **end** keyword and the **context** keyword.

    **Violation**

    .. code-block:: vhdl

       end;

       end   context;

    **Fix**

    .. code-block:: vhdl

       end;

       end context;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'context', '018', token.end_keyword, token.end_context_keyword)
        self.solution = 'Reduce spaces between *end* keyword and *context* keyword to a single space.'
