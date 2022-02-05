
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.context_reference.selected_name)


class rule_004(token_case_with_prefix_suffix):
    '''
    This rule checks the context selected names have proper case in the context reference.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       context C1;

       context CON1, Con2;

    **Fix**

    .. code-block:: vhdl

       context c1;

       context con1, con2;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'context_ref', '004', lTokens)
        self.groups.append('case::name')
