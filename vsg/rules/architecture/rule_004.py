
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_004(token_case):
    '''
    Entity rule 004 checks the architecture keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '004', [token.architecture_keyword])
