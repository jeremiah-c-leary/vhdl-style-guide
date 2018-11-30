
from vsg.rules import lower_case_rule


class rule_018(lower_case_rule):
    '''
    Entity rule 018 checks the case keyword is lower case in end case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'case', '018', 'isEndCaseKeyword', 'case')
        self.solution = 'Change "case" keyword to lowercase.'
