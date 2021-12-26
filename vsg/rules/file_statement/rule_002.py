
from vsg.rules import token_case

from vsg import token

lTokens = []
lTokens.append(token.file_declaration.file_keyword)


class rule_002(token_case):
    '''
    This rule checks the **file** keyword has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is

         FILE defaultImage : load_file_type open read_mode is load_file_name;

       begin

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is

         file defaultImage : load_file_type open read_mode is load_file_name;

       begin
    '''

    def __init__(self):
        token_case.__init__(self, 'file', '002', lTokens)
        self.groups.append('case::keyword')
