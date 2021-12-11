
from vsg import token

from vsg.rules import token_case_with_prefix_suffix

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_005(token_case_with_prefix_suffix):
    '''
    Checks the label has proper case.
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'generate', '005', lTokens)
