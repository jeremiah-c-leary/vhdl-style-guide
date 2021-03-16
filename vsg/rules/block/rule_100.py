
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.block_statement.block_label, token.block_statement.label_colon])
lTokens.append([token.block_statement.label_colon, token.block_statement.block_keyword])
lTokens.append([token.block_statement.block_keyword, token.block_statement.is_keyword])
lTokens.append([token.block_statement.block_keyword, token.block_statement.guard_open_parenthesis])
lTokens.append([token.block_statement.guard_close_parenthesis, token.block_statement.is_keyword])


class rule_100(single_space_between_token_pairs):
    '''
    Checks for a single spaces between keywords in the opening part of a block statement.
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'block', '100', lTokens)
        self.solution = 'Ensure a single space between the *package* keyword and *body* keyword and identifier and *is* keyword.'
