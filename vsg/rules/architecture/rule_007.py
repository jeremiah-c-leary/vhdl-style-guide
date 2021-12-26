
from vsg.rules import token_indent

from vsg.token import architecture_body as token


class rule_007(token_indent):
    '''
    This rule checks for spaces before the **begin** keyword.

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
        token_indent.__init__(self, 'architecture', '007', [token.begin_keyword])
