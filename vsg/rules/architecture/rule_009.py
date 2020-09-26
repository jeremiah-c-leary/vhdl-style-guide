
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_009(token_case):
    '''
    Entity rule 009 checks the *end* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '009', [token.end_keyword])
