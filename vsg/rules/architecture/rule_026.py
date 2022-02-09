
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.file_declaration.colon)
lAlign.append(token.signal_declaration.colon)
lAlign.append(token.constant_declaration.colon)
lAlign.append(token.variable_declaration.colon)
lAlign.append(token.alias_declaration.colon)
lAlign.append(token.alias_declaration.is_keyword)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_026(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks the colons are in the same column for all declarations in the architecture declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of my_entity is

         signal   wr_en : std_logic;
         signal   rd_en   : std_logic;
         constant c_period : time;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of my_entity is

         signal   wr_en    : std_logic;
         signal   rd_en    : std_logic;
         constant c_period : time;

       begin
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'architecture', '026', lAlign, token.architecture_body.is_keyword, token.architecture_body.begin_keyword, lUnless)
        self.solution = 'Align identifer.'
        self.subphase = 3
