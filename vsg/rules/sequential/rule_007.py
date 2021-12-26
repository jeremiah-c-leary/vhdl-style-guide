
from vsg.rules import insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment

from vsg import token

lTokens = []
lTokens.append(token.simple_waveform_assignment.semicolon)
lTokens.append(token.simple_force_assignment.semicolon)
lTokens.append(token.simple_release_assignment.semicolon)


class rule_007(insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment):
    '''
    This rule checks for code after a sequential assignment.

    **Violation**

    .. code-block:: vhdl

        a <= '0'; b <= '1'; c <= '0'; -- comment

    **Fix**

    .. code-block:: vhdl

        a <= '0';
        b <= '1';
        c <= '0'; -- comment
    '''

    def __init__(self):
        insert_carriage_return_after_token_if_it_is_not_followed_by_a_comment.__init__(self, 'sequential', '007', lTokens)
        self.solution = 'Move code after the ; to the next line.'
