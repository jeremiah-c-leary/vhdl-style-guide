
from vsg.rules import multiline_alignment_between_tokens

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_selected_signal_assignment.with_keyword, token.concurrent_selected_signal_assignment.semicolon])
lTokenPairs.append([token.selected_force_assignment.with_keyword, token.selected_force_assignment.semicolon])
lTokenPairs.append([token.selected_variable_assignment.with_keyword, token.selected_variable_assignment.semicolon])
lTokenPairs.append([token.selected_waveform_assignment.with_keyword, token.selected_waveform_assignment.semicolon])


class rule_400(multiline_alignment_between_tokens):
    '''
    This rule checks the alignment of multiline selected assignment statements.

    |configuring_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       with (mux_select or reset) select addr <=
       "0000" when 0,
               "0001" when 1,
            "1111" when others;

    **Fix**

    .. code-block:: vhdl

       with (mux_select or reset) select addr <=
         "0000" when 0,
         "0001" when 1,
         "1111" when others;
    '''

    def __init__(self):
        multiline_alignment_between_tokens.__init__(self, 'selected_assignment', '400', lTokenPairs)
        self.phase = 5
        self.configuration.remove('align_left')
        self.configuration.remove('align_paren')
        self.align_left = 'yes'
        self.align_paren = 'no'
        self.override = True
