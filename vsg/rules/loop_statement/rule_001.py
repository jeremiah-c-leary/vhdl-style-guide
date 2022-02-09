
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg.token import loop_statement as token

lTokens = []
lTokens.append(token.loop_keyword)


class rule_001(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    This rule checks for code after the **loop** keyword.

    **Violation**

    .. code-block:: vhdl

       loop a <= b;

    **Fix**

    .. code-block:: vhdl

       loop
         a <= b;
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'loop_statement', '001', lTokens)
        self.solution = 'Move code after **loop** to the next line.'
