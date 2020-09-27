
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import case_statement as token


class rule_020(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    Case rule 020 checks for labels after the "end case" keywords.
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'case', '020', token.end_case_label, token.end_case_label)
        self.solution = 'Remove Label'
