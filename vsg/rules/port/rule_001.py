
from vsg.rules import remove_blank_lines_above_rule


class rule_001(remove_blank_lines_above_rule):
    '''
    Port rule 001 checks for a blank line above the port keyword.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'port', '001', 'isPortKeyword')
        self.solution = 'Remove blank lines above "port" keyword.'
