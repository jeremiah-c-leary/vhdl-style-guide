
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

lUnless = []
lUnless.append([token.subprogram_body.is_keyword,token.subprogram_body.begin_keyword])


class rule_029(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks for alignment of names in attribute, type, subtype, constant, signal, variable and file declarations in the architecture declarative region.

    Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-name-alignment-rules>`_ for information on changing the configurations.

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
