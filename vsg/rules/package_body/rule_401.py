
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.alias_declaration.colon)
lAlign.append(token.alias_declaration.is_keyword)

oStart = token.package_body.is_keyword
oEnd = token.package_body.end_keyword

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_401(Rule):
    '''
    This rule checks the colons are in the same column for all declarations in the package body declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       package my_package is

         signal   wr_en : std_logic;
         signal   rd_en   : std_logic;
         constant c_period : time;

       end package my_package;

    **Fix**

    .. code-block:: vhdl

       package my_package is

         signal   wr_en    : std_logic;
         signal   rd_en    : std_logic;
         constant c_period : time;

       end package my_package;
    '''

    def __init__(self):
        Rule.__init__(self, 'package_body', '401', lAlign, oStart, oEnd, lUnless)
        self.solution = 'Align colon.'
        self.subphase = 3
