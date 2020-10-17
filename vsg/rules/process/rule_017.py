
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)


class rule_017(token_case):
    '''
    Checks the label has proper case.
    '''

    def __init__(self):
        token_case.__init__(self, 'process', '017', lTokens)
