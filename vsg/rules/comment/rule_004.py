
from vsg import parser

from vsg.rules import whitespace_before_token

lTokens = []
lTokens.append(parser.comment)


class rule_004(whitespace_before_token):
    '''
    This rule checks for at least a single space before inline comments.

    **Violation**

    .. code-block:: vhdl

       wr_en <= '1';--Write data
       rd_en <= '1';   -- Read data

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1'; --Write data
       rd_en <= '1';   -- Read data
    '''

    def __init__(self):
        whitespace_before_token.__init__(self, 'comment', '004', lTokens)
        self.solution = 'Add a single space before comment'
