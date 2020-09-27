
from vsg import parser

from vsg.rules import single_space_between_tokens

from vsg.token import case_statement_alternative as token


class rule_005(single_space_between_tokens):
    '''
    Case rule 005 checks for a single space between choices and the => operator.
    '''
    def __init__(self):
        single_space_between_tokens.__init__(self, 'case', '005', parser.todo, token.assignment)
        self.solution = 'Reduce spaces between the choices and the assignment operator.'
