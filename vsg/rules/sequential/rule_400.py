
from vsg.rules import align_tokens_in_region_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.element_association.assignment)

oStart = token.simple_waveform_assignment.assignment
oEnd = token.simple_waveform_assignment.semicolon


class rule_400(Rule):
    '''
    This rule checks the alignment the => operator in record aggregates.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       interface <= (
                     write_words => 12,
                     read_words => 32
                     address => 57
                    );

    **Fix**

    .. code-block:: vhdl

       interface <= (
                     write_words => 12,
                     read_words  => 32
                     address     => 57
                    );
    '''

    def __init__(self):
        Rule.__init__(self, lAlign, oStart, oEnd)
        self.phase = 5
        self.subphase = 3
        self.solution = 'Align =>'
        self.separate_generic_port_alignment = 'no'
        self.comment_line_ends_group = 'no'
        self.blank_line_ends_group = 'no'
        self.configuration.remove('case_control_statements_ends_group')
        self.configuration.remove('if_control_statements_ends_group')
        self.configuration.remove('loop_control_statements_ends_group')
        self.configuration.remove('separate_generic_port_alignment')
        self.configuration.append('aggregate_parens_ends_group')
        self.configuration.append('ignore_single_line_aggregates')
        self.bIncludeTillBeginningOfLine = True
