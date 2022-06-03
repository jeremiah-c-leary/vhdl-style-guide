
from vsg import token

from vsg.rules.whitespace_between_token_pairs import Rule

lTokens = []
lTokens.append([token.generic_clause.generic_keyword, token.generic_clause.open_parenthesis])


class rule_003(Rule):
    '''
    This rule checks for a single space between the **generic** keyword and the (.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       generic    (

       generic(

    **Fix**

    .. code-block:: vhdl

       generic (

       generic (
    '''
    def __init__(self):
        Rule.__init__(self, 'generic', '003', lTokens)
