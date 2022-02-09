
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.block_statement.block_label)


class rule_500(token_case_with_prefix_suffix):
    '''
    This rule checks the label has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       BLOCK_LABEL : block is

    **Fix**

    .. code-block:: vhdl

       block_label : block is
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'block', '500', lTokens)
        self.groups.append('case::label')
