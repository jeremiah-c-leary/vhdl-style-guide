
from vsg.rules import token_case_with_prefix_suffix

from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.architecture_simple_name)


class rule_011(token_case_with_prefix_suffix):
    '''
    Entity rule 011 checks the architecture simple name has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'architecture', '011', lTokens)
