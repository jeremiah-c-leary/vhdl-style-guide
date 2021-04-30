
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)

oStart = token.package_declaration.is_keyword
oEnd = token.package_declaration.end_keyword

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_400(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Aligns colons for file, signal, constant and variable declarations in the package_declarative_part.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'package', '400', lAlign, oStart, oEnd, lUnless)
        self.solution = 'Align colon.'
        self.subphase = 3
