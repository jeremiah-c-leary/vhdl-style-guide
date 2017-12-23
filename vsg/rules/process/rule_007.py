
from vsg.rules import single_space_after_rule


class rule_007(single_space_after_rule):
    '''
    Process rule 007 checks for a single space between the "end" and "process" keywords.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'process', '007', 'isEndProcess', 'end')
        self.solution = 'Ensure there are only one space between the "end" and "process" keywords.'
