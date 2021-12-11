
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.process_label)


class rule_017(token_case_with_prefix_suffix):
    '''
    Checks the label has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'process', '017', lTokens)
