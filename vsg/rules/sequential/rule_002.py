
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.simple_force_assignment.assignment, token.simple_force_assignment.force_keyword])
lTokens.append([token.simple_release_assignment.assignment, token.simple_release_assignment.release_keyword])
lTokens.append([token.simple_waveform_assignment.assignment, token.delay_mechanism.transport_keyword])
lTokens.append([token.simple_waveform_assignment.assignment, token.delay_mechanism.reject_keyword])
lTokens.append([token.simple_waveform_assignment.assignment, token.delay_mechanism.inertial_keyword])
lTokens.append([token.simple_waveform_assignment.assignment, parser.todo])


class rule_002(single_space_between_token_pairs):
    '''
    Checks for a single space after the <=.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'sequential', '002', lTokens)
        self.solution = 'Ensure a single space after the <=.'
