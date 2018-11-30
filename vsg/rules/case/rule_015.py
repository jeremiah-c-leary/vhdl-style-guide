
from vsg.rules import lower_case_rule


class rule_015(lower_case_rule):
    '''
    Entity rule 015 checks the is keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'case', '015', 'isCaseIsKeyword', 'is')
        self.solution = 'Change "is" keyword to lowercase.'
