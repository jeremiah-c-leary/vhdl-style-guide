
from vsg.rules import token_case as Rule

from vsg import token

lTokens = []
lTokens.append(token.selected_waveforms.when_keyword)
lTokens.append(token.selected_expressions.when_keyword)


class rule_503(Rule):
    '''
    This rule checks the **when** keyword has proper case.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" WHEN 0,
         "0001" WHEN 1,
         "1111" WHEN others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_assignment', '503', lTokens)
        self.groups.append('case::keyword')
