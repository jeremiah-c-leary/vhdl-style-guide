
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.entity_specification.colon)


class rule_100(single_space_after_token):
    '''
    This rule checks for a single space after the colon.

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
        single_space_after_token.__init__(self, 'entity_specification', '100', lTokens)
