
from vsg.rules import lowercase_word_after_colon_rule


class rule_011(lowercase_word_after_colon_rule):
    '''
    Constant rule 010 checks the constant type is lowercase.
    '''

    def __init__(self):
        lowercase_word_after_colon_rule.__init__(self, 'constant', '011', 'isConstant')
        self.solution = 'Change constant type to lowercase.'
