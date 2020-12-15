
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.postponed_keyword)


class rule_501(token_case):
    '''
    Checks the procedure call postponed keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure_call', '501', lTokens)
