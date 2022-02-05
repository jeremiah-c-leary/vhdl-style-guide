
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.loop_statement.loop_label)


class rule_503(token_case_with_prefix_suffix):
    '''
    This rule checks the proper case of the label on a loop statement.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

         LABEL : for index in 4 to 23 loop
         Label : for index in 0 to 100 loop

    **Fix**

    .. code-block:: vhdl

         label : for index in 4 to 23 loop
         label : for index in 0 to 100 loop
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'loop_statement', '503', lTokens)
        self.groups.append('case::label')
