
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

oStart = token.procedure_specification.open_parenthesis
oEnd = token.procedure_specification.close_parenthesis


class rule_004(token_indent_between_tokens):
    '''
    This rule checks the indent of parameters.

    **Violation**

    .. code-block:: vhdl

       procedure average_samples (
       constant a : in integer;
           signal b : in std_logic;
          variable c : in std_logic_vector(3 downto 0);
        signal d : out std_logic ) is
       begin
       end procedure average_samples;

    **Fix**

    .. code-block:: vhdl

       procedure average_samples (
         constant a : in integer;
         signal b : in std_logic;
         variable c : in std_logic_vector(3 downto 0);
         signal d : out std_logic ) is
       begin
       end procedure average_samples;
    '''

    def __init__(self):
        token_indent_between_tokens.__init__(self, 'procedure', '004', lTokens, oStart, oEnd)
