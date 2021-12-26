
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import port_clause as token

lTokens = []
lTokens.append(token.open_parenthesis)


class rule_016(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    This rule checks for a port definition on the same line as the **port** keyword.

    **Violation**

    .. code-block:: vhdl

       port (WR_EN    : in    std_logic;
         RD_EN    : in    std_logic;
         OVERFLOW : out   std_logic;
         DATA     : inout std_logic
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
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'port', '016', lTokens)
        self.solution = 'Move port parameter to the next line.'
