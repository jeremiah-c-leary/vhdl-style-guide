
from vsg import token

from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.if_generate_statement.if_keyword)


class rule_500(Rule):
    '''
    This rule checks the *if* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       IF condition generate

    **Fix**

    .. code-block:: vhdl

       if condition generate
    '''

    def __init__(self):
        Rule.__init__(self, 'if_generate_statement', '500', lTokens)
        self.groups.append('case::keyword')
