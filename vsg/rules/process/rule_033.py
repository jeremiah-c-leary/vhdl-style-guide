
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)

lUnless = []


class rule_033(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Checks the alignment of : in declarations in the process declarative region.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'process', '033', lAlign, token.process_statement.process_keyword, token.process_statement.begin_keyword, lUnless)
        self.solution = 'Align :\'s.'
        self.subphase = 2
