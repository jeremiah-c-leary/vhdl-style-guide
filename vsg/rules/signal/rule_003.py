
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Signal rule 003 checks there is a single space after the "signal" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'signal', '003', 'isSignal', 'signal')
        self.solution = 'Remove all but one space after the "signal" keyword.'
