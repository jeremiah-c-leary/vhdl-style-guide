
from vsg import token

from vsg.rules import token_case

lTokens = []
lTokens.append(token.case_generate_statement.end_generate_keyword)
lTokens.append(token.for_generate_statement.end_generate_keyword)
lTokens.append(token.if_generate_statement.end_generate_keyword)


class rule_010(token_case):
    '''
    This rule checks the **generate** keyword has the proper case in the **end generate** line.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       end GENERATE ram_array;

    **Fix**

    .. code-block:: vhdl

       end generate ram_array;
    '''

    def __init__(self):
        token_case.__init__(self, 'generate', '010', lTokens)
        self.groups.append('case::keyword')
