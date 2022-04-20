
from vsg.rules import single_space_between_tokens as Rule

from vsg.token import element_association
from vsg.token import choice

oLeftToken = choice.others_keyword
oRightToken = element_association.assignment


class rule_100(Rule):
    '''
    This rule checks for a single space between the **others** keyword and the => in an element_association.

    **Violation**

    .. code-block:: vhdl

       a <= (others=> (others    => '0'));

    **Fix**

    .. code-block:: vhdl

       a <= (others => (others => '0'));
    '''
    def __init__(self):
        Rule.__init__(self, 'element_association', '100', oLeftToken, oRightToken)
        self.solution = 'Ensure a single space between *others* and =>.'
