
from vsg.rules import single_space_before_rule


class rule_003(single_space_before_rule):
    '''
    Case rule 003 checks for a single space before the "is" keyword.
    '''

    def __init__(self):
        single_space_before_rule.__init__(self, 'case', '003', 'isCaseIsKeyword', 'is')
        self.solution = 'Ensure a single space exists before the "is" keyword.'
