
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.block_statement.end_block_label)


class rule_506(token_case_with_prefix_suffix):
    '''
    This rule checks the label has proper case on the end block declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end block BLOCK_LABEL;

    **Fix**

    .. code-block:: vhdl

       end block block_label;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'block', '506', lTokens)
        self.groups.append('case::label')
