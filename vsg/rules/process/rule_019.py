
from vsg.rules import token_case_with_prefix_suffix

from vsg import token

lTokens = []
lTokens.append(token.process_statement.end_process_label)


class rule_019(token_case_with_prefix_suffix):
    '''
    This rule checks the **end process** label has proper case.

    Refer to `Configuring Uppercase and Lowercase Rules <configuring_uppercase_and_lowercase_rules.html>`_ for information on changing the default case.

    **Violation**

    .. code-block:: vhdl

       end process PROC_A;

    **Fix**

    .. code-block:: vhdl

       end process proc_a;
    '''

    def __init__(self):
        token_case_with_prefix_suffix.__init__(self, 'process', '019', lTokens)
        self.groups.append('case::label')
