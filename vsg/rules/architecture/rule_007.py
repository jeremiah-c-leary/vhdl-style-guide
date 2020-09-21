
from vsg.rules import token_indent

from vsg.token import architecture_body as token


class rule_007(token_indent):
    '''
    Architecture rule 007 checks the indent of the *begin* keyword.
    '''

    def __init__(self):
        token_indent.__init__(self, 'architecture', '007', [token.begin_keyword])
