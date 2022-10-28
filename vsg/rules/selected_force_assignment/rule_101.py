
from vsg.rules.whitespace_before_token import Rule

from vsg.token import selected_force_assignment as token

lTokens = []
lTokens.append(token.select_keyword)


class rule_101(Rule):
    '''
    This rule checks for a single space before the **select** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel      select
         addr <= force "0000" when 0,
                       "0001" when 1,
                       "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select
         addr <= force "0000" when 0,
                       "0001" when 1,
                       "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_force_assignment', '101', lTokens)
