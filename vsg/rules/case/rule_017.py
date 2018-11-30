
from vsg.rules import lower_case_rule


class rule_017(lower_case_rule):
    '''
    Entity rule 016 checks the end keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'case', '017', 'isEndCaseKeyword', 'end')
        self.solution = 'Change "when" keyword to lowercase.'
