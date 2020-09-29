
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)

class rule_020(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    Component rule 020 ensures the alignment of inline comments in a component declaration.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'component', '020', lAlign, token.component_declaration.component_keyword, token.component_declaration.end_keyword, lSkip)
        self.solution = 'Align identifer.'
        self.subphase = 2
