from vsg.rules import lowercase_word_rule


class rule_004(lowercase_word_rule):
    '''
    Signal rule 004 checks the signal name is lowercase.
    '''

    def __init__(self):
        lowercase_word_rule.__init__(self, 'signal', '004', 'isSignal', 1)
        self.solution = 'Change signal name to lowercase.'
