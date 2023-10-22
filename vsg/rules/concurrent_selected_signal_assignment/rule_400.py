
from vsg.rules import multiline_conditional_alignment as Rule

from vsg import token

lTokenPairs = []
lTokenPairs.append([token.concurrent_selected_signal_assignment.assignment, token.concurrent_selected_signal_assignment.semicolon])


class rule_400(Rule):
    '''
    This rule checks alignment of multiline concurrent selected signal statements.

    |configuring_conditional_multiline_indent_rules_link|

    **Violation**

    .. code-block:: vhdl

       with mux_sel select addr <=
         c_input_data when 0,
         c_output_data when 1,
         (others => 'X') when others;

    **Fix**

    .. code-block:: vhdl

       with mux_sel select addr <=
         c_input_data    when 0,
         c_output_data   when 1,
         (others => 'X') when others;
    '''

    def __init__(self):
        Rule.__init__(self, 'concurrent_selected_signal_assignment', '400', lTokenPairs)
        self.configuration.remove('align_else_keywords')
