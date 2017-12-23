
from vsg.rules import lower_case_rule


class rule_008(lower_case_rule):
    '''
    Process rule 008 checks the "end" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'process', '008', 'isEndProcess', 'end')
        self.solution = 'Lowercase the "end" keyword.'
