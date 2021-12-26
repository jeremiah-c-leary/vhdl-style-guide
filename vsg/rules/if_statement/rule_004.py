
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([parser.close_parenthesis, token.if_statement.then_keyword])


class rule_004(single_space_between_token_pairs):
    '''
    This rule checks for a single space between the ) and the **then** keyword.

    **Violation**

    .. code-block:: vhdl

      if (a = '1')then

      if (a = '1')    then

    **Fix**

    .. code-block:: vhdl

      if (a = '1') then

      if (a = '1') then
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'if', '004', lTokens)
        self.solution = 'Ensure only a single space exists between the ) and *then* keyword.'
