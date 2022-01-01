
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.incomplete_type_declaration.identifier)
lTokens.append(token.full_type_declaration.identifier)


class rule_004(token_case_with_prefix_suffix):
    '''
    This rule checks the type identifier has proper case.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       type STATE_MACHINE is (idle, write, read, done);

    **Fix**

    .. code-block:: vhdl

       type state_machine is (idle, write, read, done);
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'type', '004', lTokens)
        self.configuration.append('prefix_exceptions')
        self.configuration.append('suffix_exceptions')
        self.groups.append('case::name')
