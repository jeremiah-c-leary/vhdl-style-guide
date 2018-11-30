
from vsg.rules import lower_case_rule


class rule_013(lower_case_rule):
    '''
    Entity rule 013 checks the "is" keyword is lower case in type definitions.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'type', '013', 'isTypeKeyword', 'is')
        self.solution = 'Change "is" keyword to lowercase.'
