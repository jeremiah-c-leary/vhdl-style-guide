
from vsg import token

from vsg.rules import token_suffix

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_600(token_suffix):
    '''
    Constant rule 600 checks for suffixes in generate identifiers.
    '''

    def __init__(self):
        token_suffix.__init__(self, 'generate', '600', lTokens)
        self.suffixes = ['_gen']
