
from vsg.rules import align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token

from vsg.token import case_statement_alternative as token


class rule_021(align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token):
    '''
    Case rule 021 checks for labels after the "end case" keywords.
    '''

    def __init__(self):
        align_consecutive_lines_starting_with_a_comment_above_line_starting_with_token.__init__(self, 'case', '021', token.when_keyword)
        self.solution = 'Align comment with *when* keyword.'
