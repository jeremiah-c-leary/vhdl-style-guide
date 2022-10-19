
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens as Rule

from vsg import token

lAlign = []
lAlign.append(token.constant_declaration.assignment_operator)
lAlign.append(token.signal_declaration.assignment_operator)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword, token.subprogram_body.begin_keyword])


class rule_401(Rule):
    '''
    This rule checks the default assignment operator := are in the same column.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal   wr_en    : std_logic := '1';
       signal   rd_en    : std_logic     := '0';
       constant c_period : integer  := 20;

    **Fix**

    .. code-block:: vhdl

       signal   wr_en    : std_logic := '1';
       signal   rd_en    : std_logic := '0';
       constant c_period : time      := 20;
    '''

    def __init__(self):
        Rule.__init__(self, 'architecture', '401', lAlign, token.architecture_body.is_keyword, token.architecture_body.begin_keyword, lUnless)
        self.solution = 'Align assignment operator.'
        self.subphase = 4
