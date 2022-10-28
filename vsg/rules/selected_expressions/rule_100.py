
from vsg.rules.whitespace_before_token import Rule

from vsg.token import selected_expressions as token

lTokens = []
lTokens.append(token.when_keyword)


class rule_100(Rule):
    '''
    This rule checks for a single space before the **when** keyword.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel select
         addr := "0000"when 0,
                 "0001"    when 1,
                 "1111"  when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select
         addr := "0000" when 0,
                 "0001" when 1,
                 "1111" when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'selected_expressions', '100', lTokens)
