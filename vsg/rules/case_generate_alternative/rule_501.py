
from vsg.rules import token_case_in_range_bounded_by_tokens as Rule

from vsg import token

lTokens = []
lTokens.append(token.choice.others_keyword)

oStartToken = token.case_generate_alternative.when_keyword

oEndToken = token.case_generate_alternative.assignment


class rule_501(Rule):
    '''
    This rule checks the *others* keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       when OTHERS =>

    **Fix**

    .. code-block:: vhdl

       when others =>
    '''

    def __init__(self):
        Rule.__init__(self, 'case_generate_alternative', '501', lTokens, oStartToken, oEndToken)
        self.groups.append('case::keyword')
