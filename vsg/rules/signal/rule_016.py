
from vsg import token

from vsg.rules import remove_carriage_returns_between_token_pairs

lTokens = []
lTokens.append([token.signal_declaration.signal_keyword, token.signal_declaration.semicolon])


class rule_016(remove_carriage_returns_between_token_pairs):
    '''
    Checks a signal declaration is on a single line.
    '''

    def __init__(self):
        remove_carriage_returns_between_token_pairs.__init__(self, 'signal', '016', lTokens)
        self.solution = 'ensure signal declaration is on a single line.'
