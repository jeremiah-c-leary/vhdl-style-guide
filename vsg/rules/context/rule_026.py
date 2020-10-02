
from vsg.rules import remove_excessive_blank_lines_below_line_ending_with_token

from vsg.token import context_declaration as token


class rule_026(remove_excessive_blank_lines_below_line_ending_with_token):
    '''
    Checks for more than one blank line below the is keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_below_line_ending_with_token.__init__(self, 'context', '026', [token.is_keyword])
