
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.attribute_specification.attribute_keyword)
lTokens.append(token.attribute_specification.attribute_designator)
lTokens.append(token.attribute_specification.of_keyword)
lTokens.append(token.attribute_specification.is_keyword)


class rule_100(single_space_after_token):
    '''
    This rule checks for a single space after the following attribute_specification elements:  **attribute** keyword, *attribute_designator*, **of** keyword and **is** keyword.

    **Violation**

    .. code-block:: vhdl

       attribute   coordinate   of   comp_1:component   is   (0.0, 17.5);

       attribute   coordinate   of   comp_1:component   is(0.0, 17.5);

    **Fix**

    .. code-block:: vhdl

       attribute coordinate of comp_1:component   is (0.0, 17.5);

       attribute coordinate of comp_1:component   is (0.0, 17.5);
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'attribute_specification', '100', lTokens)
