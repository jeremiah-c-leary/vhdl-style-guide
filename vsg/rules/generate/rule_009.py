
from vsg import token

from vsg.rules import token_case

lTokens = []
lTokens.append(token.case_generate_statement.end_keyword)
lTokens.append(token.for_generate_statement.end_keyword)
lTokens.append(token.if_generate_statement.end_keyword)


class rule_009(token_case):
    '''
    This rule checks the **end** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       END generate ram_array;

    **Fix**

    .. code-block:: vhdl

       end generate ram_array;
    '''

    def __init__(self):
        token_case.__init__(self, 'generate', '009', lTokens)
        self.groups.append('case::keyword')
