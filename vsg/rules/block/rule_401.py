
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_401(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Architecture rule 401 aligns colons for file, signal, constant and variable declarations in the architecture_body.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'block', '401', lAlign, token.block_statement.block_keyword, token.block_statement.begin_keyword, lUnless)
        self.solution = 'Align colon.'
        self.subphase = 2
