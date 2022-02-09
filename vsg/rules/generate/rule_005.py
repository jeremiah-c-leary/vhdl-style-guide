
from vsg import token

from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_005(token_case_with_prefix_suffix):
    '''
    This rule checks the generate label has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       RAM_ARRAY: for i in 0 to 7 generate

    **Fix**

    .. code-block:: vhdl

       ram_array: for i in 0 to 7 generate
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'generate', '005', lTokens)
        self.groups.append('case::label')
