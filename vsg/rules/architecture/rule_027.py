
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)


class rule_027(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    Architecture rule 027 checks the alignment of inline comments in the architecture declarative part.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'architecture', '027', lAlign, token.architecture_body.is_keyword, token.architecture_body.begin_keyword, lSkip)
        self.solution = 'Align comments.'
        self.subphase = 4
