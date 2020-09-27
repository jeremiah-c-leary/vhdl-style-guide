
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import case_statement as token


class rule_019(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    Case rule 019 checks for labels before the case case keyword.
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'case', '019', token.case_label, token.label_colon)
        self.solution = 'Remove Label'
