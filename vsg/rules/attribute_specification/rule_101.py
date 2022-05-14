
from vsg import token

from vsg.rules import whitespace_before_token as Rule

lTokens = []
lTokens.append(token.attribute_specification.is_keyword)


class rule_101(Rule):
    '''
    This rule checks for a single space before the **is** keyword.

    **Violation**

    .. code-block:: vhdl

       attribute coordinate of comp_1 : component   is (0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1 : component is (0.0, 17.5);

       attribute coordinate of comp_1 : component is (0.0, 17.5);
    '''
    def __init__(self):
        Rule.__init__(self, 'attribute_specification', '101', lTokens)
