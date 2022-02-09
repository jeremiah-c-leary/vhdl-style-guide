
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.context_declaration.context_simple_name)


class rule_016(token_case_with_prefix_suffix):
    '''
    This rule checks the context identifier has proper case in the end context declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end context C1;

    **Fix**

    .. code-block:: vhdl

       end context c1;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'context', '016', lTokens)
        self.groups.append('case::name')
