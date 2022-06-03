
from vsg import token

from vsg.rules.whitespace_between_token_pairs_bounded_by_tokens import Rule

lTokens = []
lTokens.append([token.association_element.assignment, token.association_element.actual_part])

lStart = token.generic_map_aspect.open_parenthesis
lEnd = token.generic_map_aspect.close_parenthesis


class rule_007(Rule):
    '''
    This rule checks for a single space after the **=>** keyword in generic maps.

    |configuring_whitespace_rules_link|

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
        Rule.__init__(self, 'generic_map', '007', lTokens, lStart, lEnd)
