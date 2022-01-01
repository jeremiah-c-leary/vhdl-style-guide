
from vsg.rules import token_case_with_prefix_suffix

from vsg.token import architecture_body as token

lTokens = []
lTokens.append(token.architecture_simple_name)


class rule_011(token_case_with_prefix_suffix):
    '''
    This rule checks the architecture name case in the **end architecture** statement.

    Refer to the section `Configuring Uppercase and Lowercase Rules <configuring.html#configuring-uppercase-and-lowercase-rules>`_ for information on changing the default case.


    **Violation**

    .. code-block:: vhdl

       end architecture ARCHITECTURE_NAME;

    **Fix**

    .. code-block:: vhdl

       end architecture architecture_name;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'architecture', '011', lTokens)
        self.groups.append('case::name')
