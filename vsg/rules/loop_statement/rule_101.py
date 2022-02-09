
from vsg.rules import single_space_between_tokens

from vsg.token import loop_statement as token


class rule_101(single_space_between_tokens):
    '''
    This rule checks for a single space before the ending loop label if it exists.

    **Violation**

    .. code-block:: vhdl

       end loop           END_LOOP_LABEL;

    **Fix**

    .. code-block:: vhdl

       end loop END_LOOP_LABEL;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'loop_statement', '101', token.end_loop_keyword, token.end_loop_label)
        self.solution = 'Reduce spaces between **loop** keyword and label to single space.'
