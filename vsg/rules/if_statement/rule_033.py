
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token

from vsg.token import if_statement as token


class rule_033(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    '''
    Checks consecutive comment lines above an "else" keyword
    in an if statement are aligned with the "else" keyword.
    '''

    def __init__(self):
        align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token.__init__(self, 'if', '033', token.else_keyword)
        self.solution = 'Align comment with *else* keyword.'
