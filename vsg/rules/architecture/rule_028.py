
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_028(token_case):
    '''
    Entity rule 028 checks the end *architecture* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '028', [token.end_architecture_keyword])
