
from vsg.rules import single_space_before_token

from vsg.token import case_statement_alternative as token


class rule_005(single_space_before_token):
    '''
    Case rule 005 checks for a single space between choices and the => operator.
    '''
    def __init__(self):
        single_space_before_token.__init__(self, 'case', '005', [token.assignment])
        self.solution = 'Reduce spaces before the assignment operator to a single space.'
