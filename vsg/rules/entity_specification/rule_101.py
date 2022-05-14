
from vsg import token

from vsg.rules.whitespace_before_token import Rule

lTokens = []
lTokens.append(token.entity_specification.colon)


class rule_101(Rule):
    '''
    This rule checks for at least a single space before the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute coordinate of comp_1: component is (0.0, 17.5);

       attribute coordinate of comp_1     : component is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1 : component is (0.0, 17.5);

       attribute coordinate of comp_1     : component is (0.0, 17.5);
    '''
    def __init__(self):
        Rule.__init__(self, 'entity_specification', '101', lTokens)
        self.number_of_spaces = '>=1'
