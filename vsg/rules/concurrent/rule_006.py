
from vsg.rules import align_tokens_in_region_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.concurrent_simple_signal_assignment.assignment)
lAlign.append(token.concurrent_conditional_signal_assignment.assignment)


class rule_006(align_tokens_in_region_between_tokens):
    '''
    Concurrent rule 006 ensures the alignment of the "<=" keyword over multiple lines.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens.__init__(self, 'concurrent', '006', lAlign, token.architecture_body.begin_keyword, token.architecture_body.end_keyword)
        self.solution = 'Inconsistent alignment of "<=" in group of lines.'
