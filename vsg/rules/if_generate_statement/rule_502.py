
from vsg import token

from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.if_generate_statement.elsif_keyword)


class rule_502(Rule):
    '''
    This rule checks the *elsif* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       ELSIF condition generate

    **Fix**

    .. code-block:: vhdl

       elsif condition generate
    '''

    def __init__(self):
        Rule.__init__(self, 'if_generate_statement', '502', lTokens)
        self.groups.append('case::keyword')
