
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import generic_clause as token

lTokens = []
lTokens.append(token.open_parenthesis)


class rule_013(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    This rule checks for the **generic** keyword on the same line as a generic declaration.

    **Violation**

    .. code-block:: vhdl

       generic (g_depth : integer := 512;

    **Fix**

    .. code-block:: vhdl

       generic (
         g_depth : integer := 512;
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'generic', '013', lTokens)
        self.solution = 'Move generic parameter to the next line.'
