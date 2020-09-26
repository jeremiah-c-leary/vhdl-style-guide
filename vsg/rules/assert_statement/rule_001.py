
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.assertion.keyword)
lTokens.append(token.assertion.report_keyword)
lTokens.append(token.assertion.severity_keyword)
lTokens.append(token.concurrent_assertion_statement.label_name)
lTokens.append(token.assertion_statement.label)

class rule_001(token_indent):
    '''
    Assert rule 001 checks for spaces at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'assert', '001', lTokens)
