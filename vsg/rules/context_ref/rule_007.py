
from vsg import proposed_rule


class rule_007(proposed_rule.Rule):
    '''
    This rule checks for code after the semicolon.

    .. NOTE:: This rule has not been implemented yet.

    **Violation**

    .. code-block:: vhdl

       context c1; -- Comments are allowed

       context c1; library ieee; -- This is not allowed

    **Fix**

    .. code-block:: vhdl

       context c1; -- Comments are allowed

       context c1;
         library ieee; -- This is not allowed
    '''

    def __init__(self):
        proposed_rule.Rule.__init__(self, 'context_ref', '007')
