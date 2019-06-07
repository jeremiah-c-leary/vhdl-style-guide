
from vsg.rules import remove_blank_lines_above_rule


class rule_019(remove_blank_lines_above_rule):
    '''
    Generic rule 019 checks for blank lines above the closing parenthesis.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'generic', '019', 'isEndGenericMap')
        self.solution = 'Remove blank lines above ); keyword.'
