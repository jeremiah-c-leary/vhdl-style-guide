
from vsg.rules import previous_line

from vsg.token import architecture_body as token


class rule_018(previous_line):
    '''
    Architecture rule 018 checks for a blank line above the *end* keyword.
    '''

    def __init__(self):
        previous_line.__init__(self, 'architecture', '018', [token.end_keyword])
