
from vsg.rules import lower_case_rule


class rule_010(lower_case_rule):
    '''
    Entity rule 010 checks the "end" keyword is lowercase.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'entity', '010', 'isEndEntityDeclaration', 'end')
        self.solution = 'Change "end" keyword to lowercase.'
