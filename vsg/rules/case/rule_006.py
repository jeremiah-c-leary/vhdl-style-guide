
from vsg.rules import single_space_between_tokens

from vsg.token import case_statement as token


class rule_006(single_space_between_tokens):
    '''
    Case rule 006 checks for a single space between the *end* keyword and *end case* keyword.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'case', '006', token.end_keyword, token.end_case_keyword)
        self.solution = 'Reduce spaces between the *end* and *case* keywords to one space.'
