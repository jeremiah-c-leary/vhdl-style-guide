
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Signal rule 003 checks there is a single space after the "variable" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'variable', '003', 'isVariable', 'variable')
        self.solution = 'Remove all but one space after the "variable" keyword.'
