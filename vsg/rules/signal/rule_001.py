
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.signal_declaration.signal_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of signal declarations.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

       signal wr_en : std_logic;
            signal rd_en : std_logic;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         signal wr_en : std_logic;
         signal rd_en : std_logic;

       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'signal', '001', lTokens)
