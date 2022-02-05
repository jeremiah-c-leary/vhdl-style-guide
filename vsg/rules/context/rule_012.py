
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.identifier)


class rule_012(token_case_with_prefix_suffix):
    '''
    This rule checks the context identifier has proper case in the context declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       context C1 is

    **Fix**

    .. code-block:: vhdl

       context c1 is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'context', '012', lTokens)
        self.groups.append('case::name')
