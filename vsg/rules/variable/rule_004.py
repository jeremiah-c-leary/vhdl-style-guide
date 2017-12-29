
from vsg.rules import lowercase_word_rule


class rule_004(lowercase_word_rule):
    '''
    Signal rule 004 checks the variable name is lowercase.
    '''

    def __init__(self):
        lowercase_word_rule.__init__(self, 'variable', '004', 'isVariable', 1)
        self.solution = 'Change variable name to lowercase.'
