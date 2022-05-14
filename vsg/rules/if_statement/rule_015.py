
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.if_statement.end_keyword, token.if_statement.end_if_keyword])


class rule_015(Rule):
    '''
    This rule checks for a single space between the **end if** keywords.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       end    if;

    **Fix**

    .. code-block:: vhdl

       end if;
    '''
    def __init__(self):
        Rule.__init__(self, 'if', '015', lTokens)
