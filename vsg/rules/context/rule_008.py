
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.end_keyword)


class rule_008(split_line_at_token):
    '''
    This rule checks the **end** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       context c1 is library ieee; end context c1;

       context c1 is library ieee; end;

    **Fix**

    .. code-block:: vhdl

       context c1 is library ieee;
       end context c1;

       context c1 is library ieee;
       end;
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'context', '008', lTokens)
        self.solution = 'Move *end* keyword and code after end to the next line'
