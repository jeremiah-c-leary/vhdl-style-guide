
from vsg.rules import previous_line

from vsg.token import architecture_body as token


class rule_003(previous_line):
    '''
    Architecture rule 003 checks for a blank line above the architecture keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'architecture', '003', [token.architecture_keyword])
        self.style = 'require_blank_line'
