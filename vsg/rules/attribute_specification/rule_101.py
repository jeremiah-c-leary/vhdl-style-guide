
from vsg import token

from vsg.rules import single_space_before_token

lTokens = []
lTokens.append(token.attribute_specification.is_keyword)


class rule_101(single_space_before_token):
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
        single_space_before_token.__init__(self, 'attribute_specification', '101', lTokens)
