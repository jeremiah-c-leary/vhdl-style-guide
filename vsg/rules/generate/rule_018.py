
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.generate_statement_body.end_keyword)


class rule_018(token_indent):
    '''
    This rule checks the indent of the **end** keyword in the generate statement body.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
         end;
       end generate;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
       end;
       end generate;
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '018', lTokens)
