
from vsg.rules import lower_case_rule


class rule_002(lower_case_rule):
    '''
    Type rule 002 checks the "type" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'type', '002', 'isTypeKeyword', 'type')
        self.solution = 'Lowercase "type" keyword.'
