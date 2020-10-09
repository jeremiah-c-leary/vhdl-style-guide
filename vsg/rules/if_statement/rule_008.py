
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import if_statement as token

lTokens = []
lTokens.append(token.end_keyword)

class rule_008(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for an empty line before the "elsif" keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'if', '008', lTokens, iAllow=0)
        self.solution = 'Remove blank line(s) before the "end if" keyword.'
