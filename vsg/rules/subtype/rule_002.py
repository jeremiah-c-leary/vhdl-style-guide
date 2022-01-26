
from vsg import parser
from vsg import token

from vsg.rules import consistent_token_case

lTokens = []
lTokens.append(token.subtype_declaration.identifier)

lIgnore = []
lIgnore.append(token.interface_signal_declaration.identifier)
lIgnore.append(token.interface_unknown_declaration.identifier)
lIgnore.append(token.interface_constant_declaration.identifier)
lIgnore.append(token.interface_variable_declaration.identifier)
lIgnore.append(token.association_element.formal_part)
lIgnore.append(parser.whitespace)
lIgnore.append(parser.carriage_return)
lIgnore.append(parser.blank_line)


class rule_002(consistent_token_case):
    '''
    This rule checks for consistent capitalization of subtype names.

    **Violation**

    .. code-block:: vhdl

       subtype read_size is range 0 to 9;
       subtype write_size is range 0 to 9;

       signal read  : READ_SIZE;
       signal write : write_size;

       constant read_sz  : read_size := 8;
       constant write_sz : WRITE_size := 1;


    **Fix**

    .. code-block:: vhdl

       subtype read_size is range 0 to 9;
       subtype write_size is range 0 to 9;

       signal read  : read_size;
       signal write : write_size;

       constant read_sz  : read_size := 8;
       constant write_sz : write_size := 1;
    '''

    def __init__(self):
        consistent_token_case.__init__(self, 'subtype', '002', lTokens, lIgnore)
