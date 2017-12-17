
from vsg.rules import single_space_after_rule


class rule_002(single_space_after_rule):
    '''
    Entity rule 002 checks for a single space after the entity keyword.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'entity', '002', 'isEntityDeclaration', 'entity')
        self.solution = 'Remove extra spaces after entity keyword.'
