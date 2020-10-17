
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.signal_assignment_statement.label)
lTokens.append(token.simple_force_assignment.target)
lTokens.append(token.simple_waveform_assignment.target)


class rule_001(token_indent):
    '''
    Checks for the proper indentation at the beginning of the sequential statement.
    '''

    def __init__(self):
        token_indent.__init__(self, 'sequential', '001', lTokens)
