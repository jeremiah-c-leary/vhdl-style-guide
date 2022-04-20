
from vsg import token

from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.if_generate_statement.else_keyword)


class rule_503(Rule):
    '''
    This rule checks the *else* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ELSE generate

    **Fix**

    .. code-block:: vhdl

       else generate
    '''

    def __init__(self):
        Rule.__init__(self, 'if_generate_statement', '503', lTokens)
        self.groups.append('case::keyword')
