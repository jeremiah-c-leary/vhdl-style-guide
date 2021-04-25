
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.report_statement.report_keyword)
lTokens.append(token.report_statement.severity_keyword)


class rule_300(token_indent):
    '''
    Assert rule 300 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'report_statement', '300', lTokens)
