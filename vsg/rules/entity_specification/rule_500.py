
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.entity_name_list.others_keyword)


class rule_500(token_case):
    '''
    Checks the *others* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'entity_specification', '500', lTokens)
