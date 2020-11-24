
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.port_clause.port_keyword, token.port_clause.open_parenthesis])


class rule_003(single_space_between_token_pairs):
    '''
    Checks for a single space between the label and :.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'port', '003', lTokens)
        self.solution = 'Change spacing between "port" and "(" to one space.'
