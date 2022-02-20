
from vsg import token

from vsg.rules import token_case as Rule

lTokens = []
lTokens.append(token.case_generate_statement.case_keyword)


class rule_500(Rule):
    '''
    This rule checks the *case* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       CASE expression generate

    **Fix**

    .. code-block:: vhdl

       case expression generate
    '''

    def __init__(self):
        Rule.__init__(self, 'case_generate_statement', '500', lTokens)
        self.groups.append('case::keyword')
