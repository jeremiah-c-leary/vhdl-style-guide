
from vsg.rules import remove_blank_lines_below_rule


class rule_022(remove_blank_lines_below_rule):
    '''
    Port rule 022 checks for a blank line below the port keyword.
    '''

    def __init__(self):
        remove_blank_lines_below_rule.__init__(self, 'port', '022', 'isPortKeyword')
        self.solution = 'Remove blank lines below "port" keyword.'
