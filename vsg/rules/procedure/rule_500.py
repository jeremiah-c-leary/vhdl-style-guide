
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.procedure_specification.procedure_keyword)


class rule_500(token_case):
    '''
    This rule checks the **procedure** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       PROCEDURE average_samples is

    **Fix**

    .. code-block:: vhdl

       procedure average_samples is
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '500', lTokens)
        self.groups.append('case::keyword')
