
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_019(token_case):
    '''
    This rule checks the proper case of the **of** keyword in the architecture declaration.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl OF fifo is

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '019', [token.of_keyword])
        self.groups.append('case::keyword')
