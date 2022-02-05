
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.report_statement.report_keyword)


class rule_500(token_case):
    '''
    This rule checks the **report** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

        REPORT "FIFO width is limited to 16 bits."
          severity FAILURE;

    .. code-block:: vhdl

        report "FIFO width is limited to 16 bits."
          severity FAILURE;
    '''

    def __init__(self):
        token_case.__init__(self, 'report_statement', '500', lTokens)
        self.groups.append('case::keyword')
