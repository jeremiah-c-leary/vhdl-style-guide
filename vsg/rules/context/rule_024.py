
from vsg.rules import previous_line

from vsg.token import context_declaration as token


class rule_024(previous_line):
    '''
    Checks for a blank line above the end context declaration.
    '''

    def __init__(self):
        previous_line.__init__(self, 'context', '024', [token.end_keyword])
        self.style = 'no_code'
