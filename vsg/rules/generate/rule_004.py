
from vsg.rules import previous_line

from vsg import token

lTokens = []
lTokens.append(token.case_generate_statement.generate_label)
lTokens.append(token.for_generate_statement.generate_label)
lTokens.append(token.if_generate_statement.generate_label)


class rule_004(previous_line):
    '''
    This rule checks for blank lines or comments before the **generate** label.

    Refer to `Configuring Previous Line Rules <configuring.html#configuring-previous-line-rules>`_ for options.

    **Violation**

    .. code-block:: vhdl

       wr_en <= '1';
       ram_array : for i in 0 to 7 generate

    **Fix**

    .. code-block:: vhdl

       wr_en <= '1';

       ram_array : for i in 0 to 7 generate
    '''

    def __init__(self):
        previous_line.__init__(self, 'generate', '004', lTokens)
