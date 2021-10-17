
from vsg.rules import blank_line_below_line_ending_with_token

from vsg.token import case_statement_alternative as token

lTokens = []
lTokens.append(token.assignment)


class rule_200(blank_line_below_line_ending_with_token):
    '''
    Case rule 200 ensures a blank line exists below the "case" keyword.
    '''

    def __init__(self):
        blank_line_below_line_ending_with_token.__init__(self, 'case', '200', lTokens)
