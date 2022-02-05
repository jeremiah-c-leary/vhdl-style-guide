
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_028(token_case):
    '''
    This rule checks the **architecture** keyword in the **end architecture** has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end ARCHITECTURE;

       end Architecture;

    **Fix**

    .. code-block:: vhdl

       end architecture;

       end architecture;
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '028', [token.end_architecture_keyword])
        self.groups.append('case::keyword')
