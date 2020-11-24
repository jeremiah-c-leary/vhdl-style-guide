
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg import token

lTokens = []
lTokens.append(token.if_statement.then_keyword)

lOverrides = []
lOverrides.append(token.case_statement.case_label)
lOverrides.append(token.case_statement.case_keyword)


class rule_006(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    Checks for more than one blank line below the *then* keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'if', '006', lTokens, iAllow=0, lOverrides=lOverrides)
