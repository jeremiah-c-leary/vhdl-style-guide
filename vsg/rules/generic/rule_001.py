
from vsg.rules import remove_blank_lines_above_rule


class rule_001(remove_blank_lines_above_rule):
    '''
    Generic rule 001 checks for a blank line above the "generic" keyword.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'generic', '001', 'isGenericKeyword')
        self.solution = 'Remove blank lines above "generic" keyword.'
