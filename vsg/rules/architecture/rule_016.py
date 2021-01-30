
from vsg.rules import previous_line

from vsg.token import architecture_body as token


class rule_016(previous_line):
    '''
    Architecture rule 016 checks for a blank line above the "begin" keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'architecture', '016', [token.begin_keyword])
