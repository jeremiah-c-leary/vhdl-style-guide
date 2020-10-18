
from vsg import parser
from vsg import token

from vsg.rules import remove_lines_starting_with_token_between_token_pairs

lTokens = []
lTokens.append([token.simple_variable_assignment.target, token.simple_variable_assignment.semicolon])

oRemoveToken = parser.comment


class rule_006(remove_lines_starting_with_token_between_token_pairs):
    '''
    Checks for commented out lines within a multiline variable_assignment statement.
    '''

    def __init__(self):
        remove_lines_starting_with_token_between_token_pairs.__init__(self, 'variable_assignment', '006', oRemoveToken, lTokens)
        self.solution = 'Remove comments inside variable assignment'
        self.fixable = False
