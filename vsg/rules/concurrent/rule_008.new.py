
from vsg.rules import align_inline_comments_between_tokens_unless_between_tokens

from vsg import parser
from vsg import token

lEnd = []
lEnd.append(token.concurrent_simple_signal_assignment.semicolon)
lEnd.append(token.concurrent_conditional_signal_assignment.semicolon)
lEnd.append(token.concurrent_selected_signal_assignment.semicolon)

lBetween = [token.architecture_body.begin_keyword, token.architecture_body.end_keyword]

lUnless

class rule_008(align_comments_on_lines_which_end_with_tokens_between_tokens):
    '''
    Ensures the alignment of inline comments in sequential concurrent statements.
    '''

    def __init__(self):
        align_comments_on_lines_which_end_tokens_between_tokens.__init__(self, 'concurrent', '008', lEnd, lBetween)
        self.subphase = 2
