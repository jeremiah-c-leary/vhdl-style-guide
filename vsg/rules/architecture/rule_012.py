
from vsg.rules import single_space_after_rule


class rule_012(single_space_after_rule):
    '''
    Architecture rule 012 checks for a single space between the "end" and "architecture" keywords.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'architecture', '012', 'isEndArchitecture', 'end')
        self.solution = 'Single space between "end" and "architecture" keywords.'
