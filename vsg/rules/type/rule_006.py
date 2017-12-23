
from vsg.rules import single_space_before_rule


class rule_006(single_space_before_rule):
    '''
    Type rule 006 checks for a single space before the "is" keyword.
    '''

    def __init__(self):
        single_space_before_rule.__init__(self, 'type', '006', 'isTypeKeyword', 'is')
        self.solution = 'Ensure a single space before the "is" keyword.'
