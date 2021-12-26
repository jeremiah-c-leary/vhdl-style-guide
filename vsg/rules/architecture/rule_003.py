
from vsg.rules import previous_line

from vsg.token import architecture_body as token


class rule_003(previous_line):
    '''
    This rule checks for a blank lines or comments above the **architecture** declaration.

    Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

    **Violation**

    .. code-block:: vhdl

       library ieee;
       architecture rtl of fifo is

    **Fix**

    .. code-block:: vhdl

       library ieee;

       architecture rtl of fifo is
    '''

    def __init__(self):
        previous_line.__init__(self, 'architecture', '003', [token.architecture_keyword])
        self.style = 'require_blank_line'
