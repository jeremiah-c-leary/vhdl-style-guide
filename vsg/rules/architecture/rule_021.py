
from vsg.rules import token_case

from vsg.token import architecture_body as token


class rule_021(token_case):
    '''
    This rule checks the proper case of the **begin** keyword.

    |configuring_uppercase_and_lowercase_rules_link|

    **Violation**

    .. code-block:: vhdl

       architecture rtl of fifo is
       BEGIN

    **Fix**

    .. code-block:: vhdl

       architecture rtl of fifo is
       begin
    '''

    def __init__(self):
        token_case.__init__(self, 'architecture', '021', [token.begin_keyword])
        self.groups.append('case::keyword')
