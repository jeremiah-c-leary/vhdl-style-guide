
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.file_declaration.file_keyword)


class rule_002(token_case):
    '''
    Checks the "file" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'file', '002', lTokens)
