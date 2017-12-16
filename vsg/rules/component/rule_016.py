
from vsg.rules import remove_blank_lines_above_rule


class rule_016(remove_blank_lines_above_rule):
    '''
    Component rule 016 checks for a blank line above the "end component" keywords.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'component', '016', 'isComponentEnd')
        self.solution = 'Remove blank line(s) above "end component" keywords.'
