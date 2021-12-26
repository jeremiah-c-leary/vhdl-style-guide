
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.end_keyword)


class rule_002(token_indent):
    '''
    This rule checks for indentation of the **end loop** keywords.
    The **end loop** must line up with the **while** keyword.
    Proper indentation enhances comprehension.

    **Violation**

    .. code-block:: vhdl

       begin

         while (temp /= 0) loop
           temp := temp/2;
             end loop;

    **Fix**

    .. code-block:: vhdl

       begin

         while (temp /= 0) loop
           temp := temp/2;
         end loop;
    '''

    def __init__(self):
        token_indent.__init__(self, 'while_loop', '002', lTokens)
