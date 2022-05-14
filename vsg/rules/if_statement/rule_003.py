
from vsg import parser
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.if_statement.if_keyword, parser.open_parenthesis])


class rule_003(Rule):
    '''
    This rule checks for a single space between the **if** keyword and the (.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

      if(a = '1') then

      if   (a = '1') then

    **Fix**

    .. code-block:: vhdl

      if (a = '1') then

      if (a = '1') then
    '''
    def __init__(self):
        Rule.__init__(self, 'if', '003', lTokens)
