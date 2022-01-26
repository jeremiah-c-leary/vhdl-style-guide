
from vsg import token

from vsg.rules import single_space_between_token_pairs_bounded_by_tokens

lTokens = []
lTokens.append([token.association_element.assignment, token.association_element.actual_part])

lStart = token.generic_map_aspect.open_parenthesis
lEnd = token.generic_map_aspect.close_parenthesis


class rule_007(single_space_between_token_pairs_bounded_by_tokens):
    '''
    This rule checks for a single space after the **=>** keyword in generic maps.

    **Violation**

    .. code-block:: vhdl

       generic map
       (
         WIDTH =>    32,
         DEPTH => 512
       )

    **Fix**

    .. code-block:: vhdl

       generic map
       (
         WIDTH => 32,
         DEPTH => 512
       )
    '''
    def __init__(self):
        single_space_between_token_pairs_bounded_by_tokens.__init__(self, 'generic_map', '007', lTokens, lStart, lEnd)
        self.solution = 'Only a single space after => operator.'
