
from vsg.rules import single_space_after_token

from vsg import token

lTokens = []
lTokens.append(token.concurrent_simple_signal_assignment.assignment)
lTokens.append(token.concurrent_conditional_signal_assignment.assignment)
lTokens.append(token.concurrent_selected_signal_assignment.assignment)


class rule_002(single_space_after_token):
    '''
    Concurrent rule 002 checks there is a single space after the assignment.
    '''

    def __init__(self):
        single_space_after_token.__init__(self, 'concurrent', '002', lTokens)
