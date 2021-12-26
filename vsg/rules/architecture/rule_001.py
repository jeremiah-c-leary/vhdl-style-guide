
from vsg.rules import token_indent

from vsg.token import architecture_body as token


class rule_001(token_indent):
    '''
    This rule checks for blank spaces before the **architecture** keyword.

    **Violation**

    .. code-block:: vhdl

         architecture rtl of fifo is
       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'architecture', '001', [token.architecture_keyword])
