
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.subprogram_body.end_keyword)


class rule_504(token_case):
    '''
    Checks the procedure end keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure', '504', lTokens)
