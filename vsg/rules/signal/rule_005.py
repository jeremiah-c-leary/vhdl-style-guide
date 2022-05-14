
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.signal_declaration.colon)


class rule_005(Rule):
    '''
    This rule checks for a single space after the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal wr_en :    std_logic;
       signal rd_en :std_logic;

    **Fix**

    .. code-block:: vhdl

       signal wr_en : std_logic;
       signal rd_en : std_logic;
    '''
    def __init__(self):
        Rule.__init__(self, 'signal', '005', lTokens)
