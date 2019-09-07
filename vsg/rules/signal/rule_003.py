
from vsg.rules import multiple_spaces_after_rule


class rule_003(multiple_spaces_after_rule):
    '''
    Signal rule 003 checks there is a single space after the "signal" keyword.
    '''

    def __init__(self):
        multiple_spaces_after_rule.__init__(self, 'signal', '003', 'isSignal', 'signal')
