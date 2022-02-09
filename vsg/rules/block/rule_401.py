
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


class rule_401(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks the colons are in the same column for all declarations in the block declarative part.

    |configuring_keyword_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal sig1: natural;
       variable var2  : natural;
       constant c_period : time;
       file my_test_input : my_file_type;

    **Fix**

    .. code-block:: vhdl

       signal sig1        : natural;
       variable var2      : natural;
       constant c_period  : time;
       file my_test_input : my_file_type;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'block', '401', lAlign, token.block_statement.block_keyword, token.block_statement.begin_keyword, lUnless)
        self.solution = 'Align colon.'
        self.subphase = 2
