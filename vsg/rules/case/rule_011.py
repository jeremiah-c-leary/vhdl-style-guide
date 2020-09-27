
from vsg.rules import align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token

from vsg.token import case_statement_alternative as token


class rule_011(align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token):
    '''
    Case rule 011 checks for labels after the "end case" keywords.
    '''

    def __init__(self):
        align_consecutive_lines_after_line_starting_with_token_and_stopping_with_token.__init__(self, 'case', '011', token.when_keyword, token.assignment)
        self.solution = 'Align one space after *when* keyword'
