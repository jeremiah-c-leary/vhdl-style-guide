
from vsg.rules import remove_blank_lines_above_rule


class rule_024(remove_blank_lines_above_rule):
    '''
    Port rule 024 checks for blank lines above the closing parenthesis.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'port', '024', 'isEndPortMap')
        self.solution = 'Remove blank lines above ); keyword.'
