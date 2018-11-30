
from vsg.rules import lower_case_rule


class rule_016(lower_case_rule):
    '''
    Entity rule 016 checks the when keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'case', '016', 'isCaseWhenKeyword', 'when')
        self.solution = 'Change "when" keyword to lowercase.'
