
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

oStart = token.process_statement.process_keyword
oEnd = token.process_statement.begin_keyword

lSkip = []
lSkip.append(parser.comment)


class rule_034(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    Ensures the alignment of inline comments in an process.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'process', '034', lAlign, oStart, oEnd, lSkip)
        self.solution = 'Align comment.'
        self.subphase = 3
        self.blank_line_ends_group = False
        self.comment_line_ends_group = False
