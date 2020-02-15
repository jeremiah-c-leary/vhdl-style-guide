
from vsg.rules import line_above_rule

class rule_003(line_above_rule):
    '''
    Entity rule 003 checks for a blank line above the entity keyword.
    '''

    def __init__(self):
        line_above_rule.__init__(self, 'entity', '003', 'isEntityDeclaration')
        self.solution = 'Add blank line above entity keyword.'
