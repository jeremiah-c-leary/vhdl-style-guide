
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)

oStart = token.package_declaration.is_keyword
oEnd = token.package_declaration.end_keyword


class rule_401(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    Checks the alignment of inline comments in the architecture declarative part.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'package', '401', lAlign, oStart, oEnd, lSkip)
        self.solution = 'Align comments.'
        self.subphase = 4
