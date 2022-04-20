
from vsg import token

from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.for_generate_statement.for_keyword)


class rule_500(Rule):
    '''
    This rule checks the *for* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       FOR x in range (3 downto 0) generate

    **Fix**

    .. code-block:: vhdl

       for x in range (3 downto 0) generate
    '''

    def __init__(self):
        Rule.__init__(self, 'for_generate_statement', '500', lTokens)
        self.groups.append('case::keyword')
