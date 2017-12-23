
from vsg.rules import lower_case_rule


class rule_002(lower_case_rule):
    '''
    Signal rule 002 checks the "signal" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'signal', '002', 'isSignal', 'signal')
