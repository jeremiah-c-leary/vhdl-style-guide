
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.concurrent_procedure_call_statement.label_name)
lTokens.append(token.procedure_call_statement.label)


class rule_500(token_case):
    '''
    Checks the procedure call label has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'procedure_call', '500', lTokens)
