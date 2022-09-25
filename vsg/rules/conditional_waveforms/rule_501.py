
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.conditional_waveforms.else_keyword)


class rule_501(Rule):
    '''
    This rule checks the **else** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') ELSE '1';

    **Fix**

    .. code-block:: vhdl

       wr_en <= '0' when (rd_en = '0') else '1';
    '''

    def __init__(self):
        Rule.__init__(self, 'conditional_waveforms', '501', lTokens)
        self.groups.append('case::keyword')
