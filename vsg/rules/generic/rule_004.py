
from vsg.rules import token_indent_between_tokens

from vsg import token

lTokens = []
lTokens.append(token.interface_constant_declaration.constant_keyword)
lTokens.append(token.interface_signal_declaration.signal_keyword)
lTokens.append(token.interface_variable_declaration.variable_keyword)
lTokens.append(token.interface_file_declaration.file_keyword)
lTokens.append(token.interface_unknown_declaration.identifier)
lTokens.append(token.interface_incomplete_type_declaration.type_keyword)
lTokens.append(token.interface_procedure_specification.procedure_keyword)
lTokens.append(token.interface_function_specification.function_keyword)
lTokens.append(token.interface_package_declaration.package_keyword)

oStart = token.generic_clause.open_parenthesis
oEnd = token.generic_clause.close_parenthesis


class rule_004(token_indent_between_tokens):
    '''
    This rule checks the indent of generic declarations.

    **Violation**

    .. code-block:: vhdl

       generic (
       g_width : integer := 32;
              g_depth : integer := 512
       )

    **Fix**

    .. code-block:: vhdl

       generic (
         g_width : integer := 32;
         g_depth : integer := 512
       )
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'generic', '004', lTokens, oStart, oEnd)
