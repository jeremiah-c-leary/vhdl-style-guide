
from vsg.rules import single_space_after_rule


class rule_006(single_space_after_rule):
    '''
    Case rule 006 checks for a single space between the "end" and "case" keywords.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'case', '006', 'isEndCaseKeyword', 'end')
        self.solution = 'Ensure a single space exists between the "end" and "case" keywords.'
