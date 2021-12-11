
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.simple_waveform_assignment.assignment)
lAlign.append(token.simple_force_assignment.assignment)
lAlign.append(token.simple_release_assignment.assignment)
lAlign.append(token.simple_variable_assignment.assignment)
lAlign.append(token.conditional_variable_assignment.assignment)

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword

lUnless = []


class rule_400(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    Ensures the alignment of the "<=" and ":=" tokens over multiple lines.
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'process', '400', lAlign, oStart, oEnd, lUnless)
        self.solution = 'Align identifer.'
        self.if_control_statements_ends_group = True
        self.case_control_statements_ends_group = True
        self.case_keyword_statements_ends_group = True
        self.loop_control_statements_ends_group = True
