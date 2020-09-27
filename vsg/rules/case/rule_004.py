
from vsg import parser

from vsg.rules import single_space_between_tokens

from vsg.token import case_statement_alternative as token


class rule_004(single_space_between_tokens):
    '''
    Case rule 004 checks for a single space between the expression and the *is* keyword.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'case', '004', token.when_keyword, parser.todo)
        self.solution = 'Reduce spaces between the *when* keyword and choices to a single space.'
