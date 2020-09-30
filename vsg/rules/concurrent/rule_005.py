
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import concurrent_signal_assignment_statement as token


class rule_005(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    Concurrent rule 005 checks for labels on concurrent assignments.
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'concurrent', '005', token.label_name, token.label_colon)
        self.solution = 'Remove Label'
