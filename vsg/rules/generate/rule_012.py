
from vsg import token

from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.case_generate_statement.end_generate_label)
lTokens.append(token.for_generate_statement.end_generate_label)
lTokens.append(token.if_generate_statement.end_generate_label)


class rule_012(token_case_with_prefix_suffix):
    '''
    This rule checks the **end generate** label has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end generate RAM_ARRAY;

    **Fix**

    .. code-block:: vhdl

       end generate ram_array;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'generate', '012', lTokens)
        self.groups.append('case::label')
