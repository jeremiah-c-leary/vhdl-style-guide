
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import use_clause as token

lTokens = []
lTokens.append(token.keyword)

class rule_007(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Removes blank lines above the "use" keyword.
    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'library', '007', lTokens, iAllow=0)
        self.solution = 'Remove blank line(s) above the *use* keyword.'
