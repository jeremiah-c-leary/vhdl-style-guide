
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.concurrent_signal_assignment_statement.label_name)
lTokens.append(token.concurrent_signal_assignment_statement.postponed_keyword)
lTokens.append(token.concurrent_simple_signal_assignment.target)
lTokens.append(token.concurrent_conditional_signal_assignment.target)
lTokens.append(token.concurrent_selected_signal_assignment.with_keyword)


class rule_001(token_indent):
    '''
    Concurrent rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'concurrent', '001', lTokens)
