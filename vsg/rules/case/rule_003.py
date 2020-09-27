
from vsg import parser

from vsg.rules import single_space_between_tokens

from vsg.token import case_statement as token


class rule_003(single_space_between_tokens):
    '''
    Case rule 003 checks for a single space between the expression and the *is* keyword.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'case', '003', parser.todo, token.is_keyword)
        self.solution = 'Reduce spaces between the expression and the *is* keyword.'
