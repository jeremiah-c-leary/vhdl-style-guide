
from vsg import proposed_rule


class rule_006(proposed_rule.Rule):
    '''
    This rule checks the semicolon is on the same line as the context selected name.

    .. NOTE:: This rule has not been implemented yet.

    **Violation**

    .. code-block:: vhdl

       context c1
       ;

       context
       c1
       ;

    **Fix**

    .. code-block:: vhdl

       context c1;

       context
       c1;
    '''

    def __init__(self):
        proposed_rule.Rule.__init__(self, 'context_ref', '006')
