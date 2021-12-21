
from vsg.rules import token_case_with_prefix_suffix

from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.entity_name)


class rule_014(token_case_with_prefix_suffix):
    '''
    Entity rule 014 checks the entity name has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'architecture', '014', lTokens)
        self.groups.append('case::name')
