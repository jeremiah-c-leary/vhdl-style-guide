
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens

from vsg import token


class rule_013(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens):
    '''
    This rule checks for multiple ports declared on a single line.

    **Violation**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;DATA     : inout std_logic
       );

    **Fix**

    .. code-block:: vhdl

       port (
         WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic
       );
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment_when_between_tokens.__init__(self, 'port', '013', [token.interface_list.semicolon], token.port_clause.open_parenthesis, token.port_clause.close_parenthesis)
        self.solution = 'Move multiple ports to their own lines.'
