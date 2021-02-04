
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.library_clause.keyword)


class rule_003(previous_line):
    '''
    Checks for a blank line above the "library" keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'library', '003', lTokens)
        self.allow_library_clause = False
        self.configuration.append('allow_library_clause')
        self.style = 'require_blank_line'

    def _set_allow_tokens(self):
        if self.allow_library_clause:
            self.lAllowTokens = []
            self.lAllowTokens.append(token.library_clause.keyword)
