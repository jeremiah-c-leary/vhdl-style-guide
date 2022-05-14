
from vsg import token

from vsg.rules.whitespace_after_token import Rule

lTokens = []
lTokens.append(token.entity_specification.colon)


class rule_100(Rule):
    '''
    This rule checks for a single space after the colon.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       attribute coordinate of comp_1 :component is (0.0, 17.5);
       attribute coordinate of comp_1 :    component is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1 : component is (0.0, 17.5);
       attribute coordinate of comp_1 : component is (0.0, 17.5);
    '''
    def __init__(self):
        Rule.__init__(self, 'entity_specification', '100', lTokens)
