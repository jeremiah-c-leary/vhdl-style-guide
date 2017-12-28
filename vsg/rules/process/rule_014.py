
from vsg.rules import single_space_before_rule


class rule_014(single_space_before_rule):
    '''
    Process rule 014 checks for a single space between the ) and "is" keyword.
    '''

    def __init__(self):
        single_space_before_rule.__init__(self, 'process', '014', 'isSensitivityListEnd', 'is')
        self.solution = 'Ensure only a single space exists between the ) and "is" keyword.'
