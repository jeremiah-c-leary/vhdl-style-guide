
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.simple_waveform_assignment.assignment)
lTokens.append(token.simple_force_assignment.assignment)
lTokens.append(token.simple_release_assignment.assignment)
lTokens.append(token.selected_waveform_assignment.assignment)
lTokens.append(token.selected_force_assignment.assignment)
lTokens.append(token.conditional_waveform_assignment.assignment)
lTokens.append(token.conditional_force_assignment.assignment)


class rule_002(single_space_after_token):
    '''
    Checks for at least a single space after the <=.
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'sequential', '002', lTokens)
        self.solution = 'Ensure at least a single space after the <=.'
