
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import if_statement as token

lTokens = []
lTokens.append(token.else_keyword)

class rule_010(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for an empty line before the "else" keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'if', '010', lTokens, iAllow=0)
        self.solution = 'Remove blank line(s) before the "else" keyword.'
