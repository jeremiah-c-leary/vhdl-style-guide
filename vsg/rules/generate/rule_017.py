
from vsg.rules import token_prefix

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_017(token_prefix):
    '''
    Constant rule 017 checks for prefixes in generate identifiers.
    '''

    def __init__(self):
        token_prefix.__init__(self, 'generate', '017', lTokens)
        self.prefixes = ['gen_']
