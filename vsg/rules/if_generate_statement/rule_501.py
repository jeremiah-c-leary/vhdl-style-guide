
from vsg import token

from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.if_generate_statement.generate_keyword)


class rule_501(Rule):
    '''
    This rule checks the *generate* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       if condition GENERATE
       elsif condition GENERATE
       else GENERATE

    **Fix**

    .. code-block:: vhdl

       if condition generate
       elsif condition generate
       else generate
    '''

    def __init__(self):
        Rule.__init__(self, 'if_generate_statement', '501', lTokens)
        self.groups.append('case::keyword')
