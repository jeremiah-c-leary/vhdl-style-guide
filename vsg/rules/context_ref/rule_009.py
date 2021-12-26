
from vsg import proposed_rule


class rule_009(proposed_rule.Rule):
    '''
    This rule checks for multiple selected names in a single reference.

    .. NOTE:: This rule has not been implemented yet.

    **Violation**

    .. code-block:: vhdl

       context c1, c2, c3; -- Comment 1

       context c1,
               c2,
               c3;

    .. code-block:: vhdl

       context c1;
       context c2;
       context c3;

       context c1;
       context c2;
       context c3;
    '''

    def __init__(self):
        proposed_rule.Rule.__init__(self, 'context_ref', '009')
