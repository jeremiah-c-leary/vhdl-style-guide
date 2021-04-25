
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.report_statement.severity_keyword)


class rule_501(token_case):
    '''
    Checks the "severity" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'report_statement', '501', lTokens)
