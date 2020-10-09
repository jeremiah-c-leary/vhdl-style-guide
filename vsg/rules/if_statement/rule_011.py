
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg.token import if_statement as token


class rule_011(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    Checks for an empty line after the "else" keyword.
    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'if', '011', [token.else_keyword], iAllow=0)
        self.solution = 'Remove blank line(s) after the "else" keyword.'
