
from vsg.rules import align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens

from vsg import parser
from vsg import token

lAlign = []
lAlign.append(parser.comment)

lSkip = []
lSkip.append(parser.comment)

oStart = token.package_declaration.is_keyword
oEnd = token.package_declaration.end_keyword


class rule_401(align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens):
    '''
    This rule checks the alignment of inline comments in the package declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       package my_package is

         signal   wr_en    : std_logic;  -- Comment 1
         signal   rd_en    : std_logic;     -- Comment 2
         constant c_period : time; -- Comment 3

       end package my_package;

    **Fix**

    .. code-block:: vhdl

       package my_package is

         signal   wr_en    : std_logic; -- Comment 1
         signal   rd_en    : std_logic; -- Comment 2
         constant c_period : time;      -- Comment 3

       end package my_package;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_skipping_lines_starting_with_tokens.__init__(self, 'package', '401', lAlign, oStart, oEnd, lSkip)
        self.solution = 'Align comments.'
        self.subphase = 4
