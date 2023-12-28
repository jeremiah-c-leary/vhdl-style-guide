
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.assertion.severity_keyword)


class rule_502(token_case):
    '''
    This rule checks the **severity** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         SEVERITY FAILURE;

    .. code-block:: vhdl

       assert WIDTH > 16
         report "FIFO width is limited to 16 bits."
         severity FAILURE;
    '''

    def __init__(self):
        token_case.__init__(self, 'assert', '502', lTokens)
        self.groups.append('case::keyword')
