
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_keyword)


class rule_300(token_indent):
    '''
    This rule checks the indentation of the **loop** keyword.

    **Violation**

    .. code-block:: vhdl

       fifo_proc : process () is
       begin

           loop

         end loop;

       end process;

    **Fix**

    .. code-block:: vhdl

       fifo_proc : process () is
       begin

         loop

         end loop;

       end process;
    '''

    def __init__(self):
        token_indent.__init__(self, 'loop_statement', '300', lTokens)
