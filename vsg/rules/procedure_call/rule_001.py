
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import procedure_call_statement as token


class rule_001(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    Checks for labels on procedure_call_statements.
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'procedure_call', '001', token.label, token.label_colon)
        self.solution = 'Remove Label'
