
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import port_map_aspect as token

lTokens = []
lTokens.append(token.open_parenthesis)


class rule_005(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    This rule checks for a port assignment on the same line as the **port map** keyword.

    **Violation**

    .. code-block:: vhdl

         port map (WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );

    **Fix**

    .. code-block:: vhdl

         port map (
           WR_EN    => wr_en,
           RD_EN    => rd_en,
           OVERFLOW => overflow
         );
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'port_map', '005', lTokens)
        self.solution = 'Move port assignment to it\'s own line.'
