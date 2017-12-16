
from vsg.rules import remove_blank_lines_above_rule


class rule_007(remove_blank_lines_above_rule):
    '''
    Library rule 007 checks for a blank line above the "use" keyword.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'library', '007', 'isLibraryUse')
        self.solution = 'Remove blank line(s) above "use" keyword.'
