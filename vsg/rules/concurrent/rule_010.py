
from vsg.rules import blank_lines_between_token_pairs

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_simple_signal_assignment.target, token.concurrent_simple_signal_assignment.semicolon])
lTokenPairs.append([token.concurrent_conditional_signal_assignment.target, token.concurrent_conditional_signal_assignment.semicolon])
lTokenPairs.append([token.concurrent_selected_signal_assignment.with_keyword, token.concurrent_selected_signal_assignment.semicolon])


class rule_010(blank_lines_between_token_pairs):
    '''
    Checks for blank lines within concurrent signal assignments.
    '''

    def __init__(self):
        blank_lines_between_token_pairs.__init__(self, 'concurrent', '010', lTokenPairs)
