
from vsg import token

from vsg.rules import single_space_after_token

lTokens = []
lTokens.append(token.report_statement.severity_keyword)


class rule_101(single_space_after_token):
    '''
    Checks for a single spaces between keywords.
    '''
    def __init__(self):
        single_space_after_token.__init__(self, 'report_statement', '101', lTokens)
