
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_019(token_case):
    '''
    Entity rule 019 checks the *of* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '019', [token.of_keyword])
