
from vsg.rules import remove_blank_lines_above_rule


class rule_007(remove_blank_lines_above_rule):
    '''
    If rule 007 checks for an empty line before the "elsif" keyword.
    '''

    def __init__(self):
        remove_blank_lines_above_rule.__init__(self, 'if', '007', 'isElseIfKeyword', 'isEndCaseKeyword')
        self.solution = 'Remove blank line(s) before the "elsif" keyword.'
