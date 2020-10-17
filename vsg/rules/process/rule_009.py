
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_process_keyword)


class rule_009(token_case):
    '''
    Checks the *process* keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'process', '009', lTokens)
