
from vsg.rules import single_space_before_rule


class rule_007(single_space_before_rule):
    '''
    Entity rule 007 checks for a single space before the "is" keyword.
    '''

    def __init__(self):
        single_space_before_rule.__init__(self, 'entity', '007', 'isEntityDeclaration', 'is')
        self.solution = 'Remove extra spaces before "is" keyword.'
