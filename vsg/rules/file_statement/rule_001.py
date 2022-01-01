
from vsg.rules import token_indent

from vsg import token

lTokens = []
lTokens.append(token.file_declaration.file_keyword)
lTokens.append(token.file_open_information.open_keyword)
lTokens.append(token.file_open_information.is_keyword)


class rule_001(token_indent):
    '''
    This rule checks the indent of **file** declarations.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

       file defaultImage : load_file_type open read_mode is load_file_name;

       file defaultImage : load_file_type open read_mode
       is load_file_name;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         file defaultImage : load_file_type open read_mode is load_file_name;

         file defaultImage : load_file_type open read_mode
           is load_file_name;

       begin
    '''

    def __init__(self):
        token_indent.__init__(self, 'file', '001', lTokens)
