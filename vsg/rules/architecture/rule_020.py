
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_020(token_case):
    '''
    Entity rule 020 checks the *is* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '020', [token.is_keyword])
