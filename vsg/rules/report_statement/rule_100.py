
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.report_statement.report_keyword)


class rule_100(Rule):
    '''
    This rule checks for a single space after the **report** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

        report     "FIFO width is limited to 16 bits.";

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits.";
    '''
    def __init__(self):
        Rule.__init__(self, 'report_statement', '100', lTokens)
