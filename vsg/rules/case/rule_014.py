
from vsg.rules import lower_case_rule


class rule_014(lower_case_rule):
    '''
    Entity rule 014 checks the case keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'case', '014', 'isCaseKeyword', 'case')
        self.solution = 'Change "case" keyword to lowercase.'
