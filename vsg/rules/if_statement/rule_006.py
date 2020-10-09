
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg.token import if_statement as token


class rule_006(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    Checks for more than one blank line below the *then* keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'if', '006', [token.then_keyword], iAllow=0)
