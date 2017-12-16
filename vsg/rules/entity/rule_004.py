
from vsg.rules import lower_case_rule


class rule_004(lower_case_rule):
    '''
    Entity rule 004 checks the entity keyword is lower case.
    '''

    def __init__(self):
        lower_case_rule.__init__(self, 'entity', '004', 'isEntityDeclaration', 'entity')
        self.solution = 'Change "entity" keyword to lowercase.'
