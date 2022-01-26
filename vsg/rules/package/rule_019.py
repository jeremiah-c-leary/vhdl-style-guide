
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


class rule_019(align_tokens_in_region_between_tokens_unless_between_tokens):
    '''
    This rule checks the identifiers for all declarations are aligned in the package declarative region.

    Refer to the section `Configuring Identifier Alignment Rules <configuring.html#configuring-identifier-alignment-rules>`_ for information on changing the configurations.

    **Violation**

    .. code-block:: vhdl

       variable var1 : natural;
       signal sig1 : natural;
       constant c_period : time;

    **Fix**

    .. code-block:: vhdl

       variable var1     : natural;
       signal   sig1     : natural;
       constant c_period : time;
    '''

    def __init__(self):
        align_tokens_in_region_between_tokens_unless_between_tokens.__init__(self, 'package', '019', lAlign, token.package_declaration.is_keyword, token.package_declaration.end_keyword, lUnless)
        self.solution = 'Align identifer.'
