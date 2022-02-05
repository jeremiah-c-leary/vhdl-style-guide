
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.attribute_declaration.identifier)


class rule_501(token_case_with_prefix_suffix):
    '''
    This rule checks the *identifier* has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute MAX_DELAY : time;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'attribute_declaration', '501', lTokens)
        self.groups.append('case::name')
