
from vsg import parser
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.if_statement.elsif_keyword, parser.open_parenthesis])


class rule_005(single_space_between_token_pairs):
    '''
    Checks there is a single space between the elsif keyword and (.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'if', '005', lTokens)
        self.solution = 'Ensure only a single space exists between the *elsif* keyword and {.'
