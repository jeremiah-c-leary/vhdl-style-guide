
from vsg.rules.whitespace_after_token import Rule

from vsg.token import selected_force_assignment as token

lTokens = []
lTokens.append(token.with_keyword)


class rule_100(Rule):
    '''
    This rule checks for a single space after the **with** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       with    mux_sel select
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
        Rule.__init__(self, 'selected_force_assignment', '100', lTokens)
