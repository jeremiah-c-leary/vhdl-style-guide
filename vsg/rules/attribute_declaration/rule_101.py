
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.attribute_declaration.colon)


class rule_101(Rule):
    '''
    This rule checks for at least a single space before the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute max_delay: time;

    **Fix**

    .. code-block:: vhdl

       attribute max_delay : time;
    '''
    def __init__(self):
        Rule.__init__(self, 'attribute_declaration', '101', lTokens)
        self.number_of_spaces = '>=1'
