
from vsg.rules import remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace

from vsg.token import concurrent_procedure_call_statement as token


class rule_002(remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace):
    '''
    Checks for labels on procedure_call_statements.
    '''

    def __init__(self):
        remove_tokens_bounded_by_tokens_and_remove_trailing_whitespace.__init__(self, 'procedure_call', '002', token.label_name, token.label_colon)
        self.solution = 'Remove Label'
