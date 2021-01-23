
from vsg.rules import blank_line_above_line_starting_with_token

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_003(blank_line_above_line_starting_with_token):
    '''
    Checks for a blank line above the "library" keyword.
    '''

    def __init__(self):
        blank_line_above_line_starting_with_token.__init__(self, 'library', '003', lTokens)
        self.allow_library_clause = False
        self.configuration.append('allow_library_clause')
        self.method = 'require_blank'

    def _set_allow_tokens(self):
        if self.allow_library_clause:
            self.lAllowTokens = []
            self.lAllowTokens.append(token.library_clause.keyword)
