
from vsg.rules import token_indent

from vsg.token import architecture_body as token


class rule_001(token_indent):
    '''
    Architecture rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'architecture', '001', [token.architecture_keyword])
