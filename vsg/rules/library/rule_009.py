
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token

from vsg.token import use_clause as token


class rule_009(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    '''
    Checks consecutive comment lines above a "use" keyword are aligned.
    '''

    def __init__(self):
        align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token.__init__(self, 'library', '009', token.keyword, bIncrement=True)
        self.solution = 'Align comment with *use* keyword.'
