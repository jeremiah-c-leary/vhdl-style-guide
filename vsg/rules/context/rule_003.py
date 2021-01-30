
from vsg.rules import previous_line

from vsg.token import context_declaration as token


class rule_003(previous_line):
    '''
    Component rule 003 checks for a blank line above the context keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'context', '003', [token.context_keyword])
        self.style = 'no_code'
