
from vsg import token

from vsg.rules import single_space_after_token as Rule

lTokens = []
lTokens.append(token.element_association.assignment)


class rule_101(Rule):
    '''
    This rule checks for a single space after the => in an element_association.

    **Violation**

    .. code-block:: vhdl

       a <= (others =>(others =>     '0'));

    **Fix**

    .. code-block:: vhdl

       a <= (others => (others => '0'));
    '''
    def __init__(self):
        Rule.__init__(self, 'element_association', '101', lTokens)
