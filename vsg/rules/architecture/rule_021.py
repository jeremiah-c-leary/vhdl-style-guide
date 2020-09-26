
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_021(token_case):
    '''
    Entity rule 021 checks the *begin* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '021', [token.begin_keyword])
