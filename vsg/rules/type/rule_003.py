
from vsg.rules import single_space_after_rule


class rule_003(single_space_after_rule):
    '''
    Type rule 003 checks there is a single space after the "type" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'type', '003', 'isTypeKeyword', 'type')
        self.solution = 'Remove all but one space after the "type" keyword.'
