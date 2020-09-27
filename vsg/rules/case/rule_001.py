
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.case_statement.case_keyword)
lTokens.append(token.case_statement.end_keyword)
lTokens.append(token.case_statement_alternative.when_keyword)


class rule_001(token_indent):
    '''
    Case rule 001 checks for the proper indentation at the beginning of the line.
    '''

    def __init__(self):
        token_indent.__init__(self, 'case', '001', lTokens)
