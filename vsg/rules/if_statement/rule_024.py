
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import if_statement as token

lTokens = []
lTokens.append(token.then_keyword)


class rule_024(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    This rule checks for code after the **then** keyword.

    **Violation**

    .. code-block:: vhdl

       if (a = '1') then c <= '1';

    **Fix**

    .. code-block:: vhdl

       if (a = '1') then
         c <= '1';
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'if', '024', lTokens)
        self.solution = 'Move code after *then* keyword to the next line.'
