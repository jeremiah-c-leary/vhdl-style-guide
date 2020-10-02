
from vsg.rules import remove_excessive_blank_lines_above_line_starting_with_token

from vsg.token import context_declaration as token


class rule_027(remove_excessive_blank_lines_above_line_starting_with_token):
    '''
    Checks for more than one blank line above the is keyword.

    '''
    def __init__(self):
        remove_excessive_blank_lines_above_line_starting_with_token.__init__(self, 'context', '027', [token.end_keyword])
