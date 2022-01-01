
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.port_clause.port_keyword, token.port_clause.open_parenthesis])


class rule_003(single_space_between_token_pairs):
    '''
    This rule checks for a single space after the **port** keyword and (.

    **Violation**

    .. code-block:: vhdl

       port   (

       port(

    **Fix**

    .. code-block:: vhdl

       port (

       port (
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'port', '003', lTokens)
        self.solution = 'Change spacing between "port" and "(" to one space.'
