
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.conditional_expressions.when_keyword)


class rule_500(Rule):
    '''
    This rule checks the **when** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' WHEN (rd_en = '0') else '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') else '1';
    '''

    def __init__(self):
        Rule.__init__(self, 'conditional_expressions', '500', lTokens)
        self.groups.append('case::keyword')
