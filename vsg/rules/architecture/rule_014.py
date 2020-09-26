
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_014(token_case):
    '''
    Entity rule 014 checks the entity name has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '014', [token.entity_name])
