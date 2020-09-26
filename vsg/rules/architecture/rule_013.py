
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_013(token_case):
    '''
    Entity rule 013 checks the architecture identifier has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '013', [token.identifier])
