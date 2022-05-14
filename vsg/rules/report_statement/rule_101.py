
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.report_statement.severity_keyword)


class rule_101(Rule):
    '''
    This rule checks for a single space after the **severity** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity    FAILURE;

    **Fix**

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    '''
    def __init__(self):
        Rule.__init__(self, 'report_statement', '101', lTokens)
