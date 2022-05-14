
from vsg import parser

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(parser.comma)


class rule_007(Rule):
    '''
    This rule checks for spaces after a comma.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc : process (wr_en,rd_en,overflow) is

    **Fix**

    .. code-block:: vhdl

       proc : process (wr_en, rd_en, overflow) is
    '''

    def __init__(self):
        Rule.__init__(self, 'whitespace', '007', lTokens)
        self.number_of_spaces = '>=1'
