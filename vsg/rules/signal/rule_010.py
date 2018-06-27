
from vsg.rules import lowercase_word_after_colon_rule


class rule_010(lowercase_word_after_colon_rule):
    '''
    Signal rule 010 checks the signal type is lowercase.
    '''

    def __init__(self):
        lowercase_word_after_colon_rule.__init__(self, 'signal', '010', 'isSignal', True)
        self.solution = 'Change signal type to lowercase.'
