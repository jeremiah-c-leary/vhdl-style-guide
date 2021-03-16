
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.elsif_keyword)

lOverrides = []
lOverrides.append(token.case_statement.semicolon)


class rule_007(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for an empty line before the "elsif" keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'if', '007', lTokens, iAllow=0, lOverrides=lOverrides)
        self.solution = 'Remove blank line(s) before the *elsif* keyword.'
