
from vsg.rules import single_space_after_rule


class rule_013(single_space_after_rule):
    '''
    Entity rule 013 checks for a single space after the "entity" keyword in the closing of the entity.
    '''

    def __init__(self):
        single_space_after_rule.__init__(self, 'entity', '013', 'isEndEntityDeclaration', 'entity')
        self.solution = 'Reduce spaces after "entity" keyword to one.'
