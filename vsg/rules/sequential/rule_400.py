
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
        Rule.__init__(self, 'sequential', '400', lAlign, oStart, oEnd)
        self.phase = 5
        self.subphase = 3
        self.solution = 'Align =>'
        self.separate_generic_port_alignment = False
        self.comment_line_ends_group = False
        self.blank_line_ends_group = False
        self.configuration.remove('separate_generic_port_alignment')
        self.bIncludeTillBeginningOfLine = True
