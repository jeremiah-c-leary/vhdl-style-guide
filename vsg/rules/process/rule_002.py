
from vsg import token

from vsg.rules import single_space_between_token_pairs

lTokens = []
lTokens.append([token.process_statement.process_keyword, token.process_statement.open_parenthesis])
lTokens.append([token.process_statement.process_keyword, token.process_statement.is_keyword])
lTokens.append([token.process_statement.process_keyword, token.process_statement.begin_keyword])


class rule_002(single_space_between_token_pairs):
    '''
    Checks for a single space between the process keyword and the process logical name
    '''
    def __init__(self):
        single_space_between_token_pairs.__init__(self, 'process', '002', lTokens)
        self.solution = 'Ensure a single space after the *process* keyword.'
