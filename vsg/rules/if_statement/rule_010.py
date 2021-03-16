
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.else_keyword)

lOverrides = []
lOverrides.append(token.case_statement.semicolon)


class rule_010(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for an empty line before the "else" keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'if', '010', lTokens, iAllow=0, lOverrides=lOverrides)
        self.solution = 'Remove blank line(s) before the *else* keyword.'
