
from vsg.rules import align_tokens_in_region_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.case_generate_alternative.assignment)

oStart = token.case_generate_statement.case_keyword
oEnd = token.case_generate_statement.end_keyword


class rule_400(Rule):
    '''
    This rule checks the *=>* are aligned in case_generate_alternatives.

    .. NOTE:: The default configuration is :code:`compact_alignment`.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       gc : case I generate
         when 1 =>
         when n_order =>
         when others =>
       end generate gc;

    **Fix**

    .. code-block:: vhdl

       gc : case I generate
         when 1       =>
         when n_order =>
         when others  =>
       end generate gc;
    '''

    def __init__(self):
        Rule.__init__(self, 'case_generate_statement', '400', lAlign, oStart, oEnd)
        self.solution = 'Inconsistent alignment of "=>".'
        self.disable = True
        self.compact_alignment = True
        self.blank_line_ends_group = False
        self.comment_line_ends_group = False
        self.separate_generic_port_alignment = False
        self.configuration.remove('separate_generic_port_alignment')
