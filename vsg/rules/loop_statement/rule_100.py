
from vsg.rules import single_space_between_tokens

from vsg.token import loop_statement as token


class rule_100(single_space_between_tokens):
    '''
    This rule checks that a single space exists between the **end** and **loop** keywords

    **Violation**

    .. code-block:: vhdl

         end loop;
         end    loop;

    **Fix**

    .. code-block:: vhdl

         end loop;
         end loop;
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'loop_statement', '100', token.end_keyword, token.end_loop_keyword)
        self.solution = 'Ensure a single space is between *end* and *loop*.'
