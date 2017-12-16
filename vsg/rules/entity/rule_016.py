
from vsg.rules import remove_blank_lines_above_rule


class rule_016(remove_blank_lines_above_rule):
    '''
    Entity rule 016 checks for a blank line above the "end entity" keywords.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'entity', '016', 'isEndEntityDeclaration')
        self.solution = 'Remove blank line(s) above "end entity" keywords.'
