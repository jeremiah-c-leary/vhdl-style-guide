
from vsg import token

from vsg.rules.whitespace_between_token_pairs_bounded_by_tokens import Rule

lTokens = []
lTokens.append([token.association_element.assignment, token.association_element.actual_part])

lStart = token.port_map_aspect.open_parenthesis
lEnd = token.port_map_aspect.close_parenthesis


class rule_007(Rule):
    '''
    This rule checks for a single space after the **=>** operator in port maps.

    |configuring_whitespace_rules_link|

    **Violation**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    =>   wr_en,
           RD_EN    =>rd_en,
           OVERFLOW =>     overflow
         );

    **Fix**

    .. code-block:: vhdl

       U_FIFO : FIFO
         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
    '''
    def __init__(self):
        Rule.__init__(self, 'port_map', '007', lTokens, lStart, lEnd)
