
from vsg.rules import token_indent

from vsg.token import architecture_body as token


class rule_008(token_indent):
    '''
    This rule checks for spaces before the **end architecture** keywords.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin
         end architecture

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin
       end architecture
    '''

    def __init__(self):
        token_indent.__init__(self, 'architecture', '008', [token.end_keyword])
