
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.end_keyword)


class rule_002(split_line_at_token):
    '''
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       loop
         a <= b; end loop;

    **Fix**

    .. code-block:: vhdl

       loop
         a <= b;
       end loop;
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'loop_statement', '002', lTokens)
        self.solution = 'Move *end* keyword to the next line.'
