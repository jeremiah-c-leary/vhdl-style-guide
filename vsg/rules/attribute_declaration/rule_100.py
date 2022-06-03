
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.attribute_declaration.attribute_keyword)
lTokens.append(token.attribute_declaration.colon)


class rule_100(Rule):
    '''
    This rule checks for a single space after the following elements:  **attribute** keyword and colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute   max_delay :   time;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    '''
    def __init__(self):
        Rule.__init__(self, 'attribute_declaration', '100', lTokens)
