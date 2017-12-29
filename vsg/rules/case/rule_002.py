
from vsg.rules import single_space_after_rule


class rule_002(single_space_after_rule):
    '''
    Case rule 002 checks for a single space after the "case" keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'case', '002', 'isCaseKeyword', 'case')
        self.solution = 'Ensure a single space exists after the "case" keyword.'
