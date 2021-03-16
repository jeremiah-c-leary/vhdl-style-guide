
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.else_keyword)

lOverrides = []
lOverrides.append(token.case_statement.case_label)
lOverrides.append(token.case_statement.case_keyword)


class rule_011(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    Checks for an empty line after the "else" keyword.
    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'if', '011', lTokens, iAllow=0, lOverrides=lOverrides)
        self.solution = 'Remove blank line(s) after the *else* keyword.'
