
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.report_statement.report_keyword)


class rule_500(token_case):
    '''
    Checks the "report" keyword has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'report_statement', '500', lTokens)
