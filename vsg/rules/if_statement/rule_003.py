
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.if_statement.if_keyword, parser.open_parenthesis])


class rule_003(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the **if** keyword and the (.

    **Violation**

    .. code-block:: vhdl

      if(a = '1') then

      if   (a = '1') then

    **Fix**

    .. code-block:: vhdl

      if (a = '1') then

      if (a = '1') then
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'if', '003', lTokens)
        self.solution = 'Ensure only a single space exists between the *if* keyword and (.'
