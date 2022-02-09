
from vsg.rules import align_tokens_in_region_between_tokens_unless_between_tokens

from vsg import token

lAlign = []
lAlign.append(token.full_type_declaration.identifier)
lAlign.append(token.incomplete_type_declaration.identifier)
lAlign.append(token.file_declaration.identifier)
lAlign.append(token.signal_declaration.identifier)
lAlign.append(token.constant_declaration.identifier)
lAlign.append(token.subtype_declaration.identifier)
lAlign.append(token.variable_declaration.identifier)
lAlign.append(token.alias_declaration.alias_designator)

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_029(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks for alignment of names in alias, attribute, type, subtype, constant, signal, variable and file declarations in the architecture declarative region.

    |configuring_identifier_alignment_rules_link|

    **Violation**

    .. code-block:: vhdl

       signal    sig1 : std_logic;
       file some_file :
       variable v_var1 : std_logic;
       type t_myType : std_logic;

    **Fix**

    .. code-block:: vhdl

       signal   sig1 : std_logic;
       file     some_file :
       variable v_var1 : std_logic;
       type     t_myType : std_logic;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'architecture', '029', lAlign, token.architecture_body.is_keyword, token.architecture_body.begin_keyword, lUnless)
        self.solution = 'Align identifer.'
