
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.end_keyword)


class rule_020(split_line_at_token):
    '''
    This rule checks the **end if** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       if (a = '1') then c <= '1'; else c <= '0'; end if;

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then c <= '1'; else c <= '0';
       end if;
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'if', '020', lTokens)
        self.solution = 'Move *end if* keywords to their own line.'
