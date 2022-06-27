
from vsg.rules import split_line_at_token

from vsg import token

lTokens = []
lTokens.append(token.context_reference.keyword)


class rule_005(split_line_at_token):
    '''
    This rule checks the **context** keyword is on its own line.

    **Violation**

    .. code-block:: vhdl

       context c1 is library ieee; context con1; end context c1;

       library ieee; context con2;

    **Fix**

    .. code-block:: vhdl

       context c1 is library ieee;
       context con1; end context c1;

       library ieee;
       context con2;
    '''

    def __init__(self):
        split_line_at_token.__init__(self, 'context_ref', '005', lTokens)
        self.solution = 'Move context and code after context to the next line'
