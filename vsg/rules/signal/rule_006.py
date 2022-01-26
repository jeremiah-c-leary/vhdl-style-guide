
from vsg import token

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(token.signal_declaration.colon)


class rule_006(whitespace_before_token):
    '''
    This rule checks for at least a single space before the colon.

    **Violation**

    .. code-block:: vhdl

       signal wr_en: std_logic;
       signal rd_en   : std_logic;

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic;
       signal rd_en   : std_logic;
    '''
    def __init__(self):
        whitespace_before_token.__init__(self, 'signal', '006', lTokens)
        self.solution = 'Ensure at least a single space exists before the :'
