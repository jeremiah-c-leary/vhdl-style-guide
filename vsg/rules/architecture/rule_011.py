
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_011(token_case):
    '''
    Entity rule 011 checks the architecture simple name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '011', [token.architecture_simple_name])
