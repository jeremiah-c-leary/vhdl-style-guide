
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generate_statement_body.begin_keyword)


class rule_006(token_indent):
    '''
    This rule checks the indent of the **begin** keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
          begin

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '006', lTokens)
