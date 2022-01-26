
from vsg import proposed_rule


class rule_008(proposed_rule.Rule):
    '''
    This rule checks the context selected name is on the same line as the **context** keyword.

    .. NOTE:: This rule has not been implemented yet.

    **Violation**

    .. code-block:: vhdl

       context
       c1
       ;

    **Fix**

    .. code-block:: vhdl

       context c1

       ;
    '''

    def __init__(self):
        proposed_rule.Rule.__init__(self, 'context_ref', '008')
