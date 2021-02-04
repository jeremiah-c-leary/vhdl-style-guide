
from vsg.rules import previous_line

from vsg.token import use_clause as token

lTokens = []
lTokens.append(token.keyword)

class rule_007(previous_line):
    '''
    Removes blank lines above the "use" keyword.
    '''
    def __init__(self):
        previous_line.__init__(self, 'library', '007', lTokens)
        self.style = 'no_blank_line'
