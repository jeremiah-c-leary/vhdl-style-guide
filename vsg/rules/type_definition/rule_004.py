
from vsg.rules import lowercase_word_rule


class rule_004(lowercase_word_rule):
    '''
    Type rule 004 checks the type name is lowercase.
    '''

    def __init__(self):
        lowercase_word_rule.__init__(self, 'type', '004', 'isTypeKeyword', 1)
        self.solution = 'Change type name to lowercase.'
