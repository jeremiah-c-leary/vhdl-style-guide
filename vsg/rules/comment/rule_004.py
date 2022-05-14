
from vsg import parser

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(parser.comment)


class rule_004(Rule):
    '''
    This rule checks for at least a single space before inline comments.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'comment', '004', lTokens)
        self.number_of_spaces = '>=1'
