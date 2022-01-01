
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.end_keyword)
lTokens.append(token.for_generate_statement.end_keyword)
lTokens.append(token.if_generate_statement.end_keyword)


class rule_007(token_indent):
    '''
    This rule checks the indent of the **end generate** keyword.

    **Violation**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
         end generate ram_array;

    **Fix**

    .. code-block:: vhdl

       ram_array : for i in 0 to 7 generate
       begin
       end generate ram_array;
    '''

    def __init__(self):
        token_indent.__init__(self, 'generate', '007', lTokens)
