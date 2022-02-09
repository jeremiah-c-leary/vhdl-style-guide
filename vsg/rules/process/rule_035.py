
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

oStart = token.process_statement.begin_keyword
oEnd = token.process_statement.end_keyword

lSkip = []
lSkip.append(parser.comment)


class rule_035(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    This rule checks the alignment of inline comments between the process begin and end process lines.
    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       proc_1: process () is
       begin

         a <= '1';   -- Assert
         b <= '0';       -- Deassert
         c <= '1'; -- Enable

       end process proc_1;

    **Fix**

    .. code-block:: vhdl

       proc_1: process () is
       begin

         a <= '1'; -- Assert
         b <= '0'; -- Deassert
         c <= '1'; -- Enable

       end process proc_1;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'process', '035', lAlign, oStart, oEnd, lSkip)
        self.solution = 'Align comment.'
        self.subphase = 3
        self.blank_line_ends_group = False
        self.comment_line_ends_group = False
        self.compact_alignment = False
        self.include_lines_without_comments = True
