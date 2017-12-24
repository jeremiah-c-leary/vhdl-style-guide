
from vsg.rules import single_space_after_rule


class rule_007(single_space_after_rule):
    '''
    Type rule 007 checks for a single space after the "is" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'type', '007', 'isTypeKeyword', 'is')
        self.solution = 'Ensure a single space after the "is" keyword.'
